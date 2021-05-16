window.onload = function() {
    var btnSidebarCollapser = document.getElementById("sidebarCollapser");
    var sidebar = document.getElementById("sidebar");
    btnSidebarCollapser.onclick = function() {
        sidebar.classList.toggle("active");
    }
}
