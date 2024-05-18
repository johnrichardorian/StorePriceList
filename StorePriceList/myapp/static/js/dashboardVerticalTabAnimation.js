function openTab(event, tabName) {
    // Get all elements with class "tabContent" and hide them
    var tabContent = document.getElementsByClassName("tabContent");
    for (var i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }

    // Get all elements with class "tabButton" and remove the "active" class
    var tabButtons = document.getElementsByClassName("tabButton");
    for (var i = 0; i < tabButtons.length; i++) {
        tabButtons[i].className = tabButtons[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";

    // Store the active tab in local storage
    localStorage.setItem('activeTab', tabName);
}

// On page load, check local storage for the active tab and open it
window.onload = function() {
    var activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
        document.getElementById(activeTab).style.display = "block";
        var tabButtons = document.getElementsByClassName("tabButton");
        for (var i = 0; i < tabButtons.length; i++) {
            if (tabButtons[i].getAttribute('onclick').includes(activeTab)) {
                tabButtons[i].className += " active";
            } else {
                tabButtons[i].className = tabButtons[i].className.replace(" active", "");
            }
        }
    } else {
        document.getElementById("defaultOpen").click();
    }
};