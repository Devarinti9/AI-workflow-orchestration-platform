from typing import TypedDict

from langgraph.graph import END, StateGraph


class WorkflowState(TypedDict):
    title: str
    summary: str
    word_count: int
    classification: str


def summarize_node(state: WorkflowState) -> WorkflowState:
    title = state.get("title", "")
    state["summary"] = title[:100] if title else "No summary available"
    return state


def count_words_node(state: WorkflowState) -> WorkflowState:
    title = state.get("title", "")
    state["word_count"] = len(title.split()) if title else 0
    return state


def classify_node(state: WorkflowState) -> WorkflowState:
    title = state.get("title", "").lower()

    if any(word in title for word in ["error", "issue", "fail", "bug"]):
        state["classification"] = "incident"
    elif any(word in title for word in ["user", "account", "profile"]):
        state["classification"] = "user-data"
    elif any(word in title for word in ["payment", "invoice", "billing"]):
        state["classification"] = "finance"
    else:
        state["classification"] = "general"

    return state


def build_workflow():
    graph = StateGraph(WorkflowState)
    graph.add_node("summarize", summarize_node)
    graph.add_node("count_words", count_words_node)
    graph.add_node("classify", classify_node)

    graph.set_entry_point("summarize")
    graph.add_edge("summarize", "count_words")
    graph.add_edge("count_words", "classify")
    graph.add_edge("classify", END)
    return graph.compile()


workflow_app = build_workflow()


def run_workflow(title: str) -> WorkflowState:
    initial_state: WorkflowState = {
        "title": title,
        "summary": "",
        "word_count": 0,
        "classification": "",
    }
    return workflow_app.invoke(initial_state)
