const menuIcon = document.getElementById("menu-icon");
const menuList = document.getElementById("menu-list");

menuIcon.addEventListener("click", () => {
    menuList.classList.toggle("hidden");
});


// JavaScript untuk mengendalikan dropdown profil
document.getElementById("profileBtn").addEventListener("click", function (e) {
    e.preventDefault();  // Mencegah link default
    var dropdown = document.getElementById("profileDropdown");
    dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
});

// Menutup dropdown ketika mengklik di luar area dropdown
window.onclick = function (event) {
    if (!event.target.matches('#profileBtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
}