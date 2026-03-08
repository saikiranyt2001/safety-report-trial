from backend.agents.safety_advisor_agent import analyze_site

def test_agent_output():
    result = analyze_site("construction", "workers without helmets")
    assert "top_risks" in result
    assert "recommendations" in result
