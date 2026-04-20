from typing import TypedDict
from langgraph.graph import END, StateGraph


class WorkflowState(TypedDict):
    title: str
    body: str
    category: str
    summary: str


def classify_node(state: WorkflowState) -> WorkflowState:
    title = state["title"].lower()
    if "qui" in title or "dolor" in title:
        category = "high_priority"
    elif len(title) > 40:
        category = "review"
    else:
        category = "normal"

    state["category"] = category
    return state


def summarize_node(state: WorkflowState) -> WorkflowState:
    body = state["body"].strip()
    state["summary"] = body[:120] + ("..." if len(body) > 120 else "")
    return state


def build_summary(title: str, body: str) -> dict:
    graph = StateGraph(WorkflowState)
    graph.add_node("classify", classify_node)
    graph.add_node("summarize", summarize_node)
    graph.set_entry_point("classify")
    graph.add_edge("classify", "summarize")
    graph.add_edge("summarize", END)

    app = graph.compile()
    result = app.invoke({"title": title, "body": body, "category": "", "summary": ""})

    return {
        "title": title,
        "category": result["category"],
        "summary": result["summary"],
    }
