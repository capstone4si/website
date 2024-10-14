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

    const images = [
        "url('/static/img/in.jpg')",
        "url('/static/img/en.jpg')",
        "url('/static/img/un.jpg')"
    ];
    const indicators = document.querySelectorAll('.ila');
    let currentIndex = 0;

    function updateJumbotron(index) {
        if (jb) {
            jb.style.backgroundImage = images[index];
        }

        indicators.forEach((indicator, i) => {
            if (i === index) {
                indicator.classList.add('ila-active');
                indicator.classList.remove('ila');
            } else {
                indicator.classList.remove('ila-active');
                indicator.classList.add('ila');
            }
        });
    }


    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');


    prevBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
        updateJumbotron(currentIndex);
    });


    nextBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
        updateJumbotron(currentIndex);
    });


    updateJumbotron(currentIndex);

    const dialogBackground = document.getElementById('dialogBackground');
    const openDialogButton = document.getElementById('openDialog');
    const closeDialogButton = document.getElementById('closeDialog');

    // Fungsi untuk membuka dialog
    openDialogButton.addEventListener('click', function () {
        dialogBackground.style.display = 'flex'; // Tampilkan dialog
    });

    // Fungsi untuk menutup dialog
    closeDialogButton.addEventListener('click', function () {
        dialogBackground.style.display = 'none'; // Sembunyikan dialog
    });

    // Juga tutup dialog saat area luar dialog di-klik
    dialogBackground.addEventListener('click', function (e) {
        if (e.target === dialogBackground) {
            dialogBackground.style.display = 'none';
        }
    });

});