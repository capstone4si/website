document.addEventListener("DOMContentLoaded", function () {

    const menuIcon = document.getElementById("menu-icon");
    const menuList = document.getElementById("menu-list");

    menuIcon.addEventListener("click", () => {
        menuList.classList.toggle("hidden");
    });


    const icPg = document.querySelectorAll('.imgPG img');
    const jb = document.getElementById('Jumbroton');


    icPg.forEach(img => {
        img.addEventListener('click', function () {
            const parentDiv = this.parentElement;
            const bgIg = parentDiv.getAttribute('datajm');
            if (jb && bgIg) {
                jb.style.backgroundImage = `url(${bgIg.replace("url('", "").replace("')", "")})`;
            }
        });
    });
});