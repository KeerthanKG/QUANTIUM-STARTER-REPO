import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app():
    return import_app("data_processor")

def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    # Check if the header text exists
    header = dash_duo.find_element("h1").text
    assert header == "Line Graph of Pink Morsel Sales", "Header text is incorrect or missing."

def test_visualisation_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    # Check if the graph component is present
    graph = dash_duo.find_element("#Line Graph of Pink Morsel Sales")
    assert graph is not None, "The visualization (line chart) is missing."

def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    # Check if the radio button component is present
    radio_items = dash_duo.find_element("#region-selector")
    assert radio_items is not None, "The region picker (radio buttons) is missing."

    # Verify default selection
    default_selected = dash_duo.get_selected_label("#region-selector")
    assert default_selected == "All", "Default region picker selection is incorrect."