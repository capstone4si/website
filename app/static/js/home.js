document.addEventListener("DOMContentLoaded", function () {
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

    var planes = [
        {
            name: "Balai Konservasi Sumber Daya Alam Aceh",
            lat: 5.528882347086243,
            lng: 95.29385578465542,
            description: "Aceh conservation center dedicated to wildlife and natural resources.",
            image: "/static/image/gajah.png"
        },
        {
            name: "Balai Konservasi Sumber Daya Alam Sumatra Utara",
            lat: 3.5443164640814775,
            lng: 98.6982041,
            description: "Protects the forests and wildlife of Northern Sumatra.",
            image: "https://via.placeholder.com/300x150.png?text=Sumatra+Utara"
        },
        {
            name: "Balai Konservasi Sumber Daya Alam Riau",
            lat: 0.46352253940349153,
            lng: 101.41554538465542,
            description: "Focuses on the conservation of Riau's ecosystems.",
            image: "https://via.placeholder.com/300x150.png?text=Riau"
        },
        {
            name: "Balai Konservasi Sumber Daya Alam Sumatra Barat",
            lat: -0.9163861746322387,
            lng: 100.36001857910635,
            description: "Responsible for conservation efforts in West Sumatra.",
            image: "https://via.placeholder.com/300x150.png?text=Sumatra+Barat"
        },
        {
            name: "Balai Konservasi Sumber Daya Alam Bengkulu dan Lampung",
            lat: -3.796567523674085,
            lng: 102.27000216609987,
            description: "Covers both Bengkulu and Lampung regions for conservation.",
            image: "https://via.placeholder.com/300x150.png?text=Bengkulu+Lampung"
        }
    ];

    var map = L.map('map').setView([-3.0060, 115.6155], 4);
    mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; ' + mapLink + ' Contributors',
        maxZoom: 18,
    }).addTo(map);

    for (var i = 0; i < planes.length; i++) {
        (function (i) {
            var marker = new L.marker([planes[i].lat, planes[i].lng])
                .bindPopup(
                    "<img src='" + planes[i].image + "' class='popup-image'>" + // Add image
                    "<b>" + planes[i].name + "</b><br>" +
                    planes[i].description + "<br>" +
                    "<button class='close-btn' onclick='zoomOut()'>Close</button>", // Add close button
                    { className: 'custom-popup' }
                )
                .addTo(map);

            marker.on('click', function () {
                // Zoom ke lokasi saat marker diklik
                map.setView([planes[i].lat, planes[i].lng], 12); // Set zoom level sesuai kebutuhan
                marker.openPopup(); // Buka popup setelah zoom
            });
        })(i);
    };

    // Function untuk melakukan zoom out kembali
    function zoomOut() {
        map.setView([-3.0060, 115.6155], 4); // Kembali ke zoom level awal
        map.closePopup(); // Tutup semua popup
    };
    function toggleDropdown(id) {
        var dropdown = document.getElementById(id);
        var card = dropdown.parentElement;

        // Tutup semua dropdown lainnya
        document.querySelectorAll('.dropdown-content').forEach(function (content) {
            if (content !== dropdown) {
                content.style.display = 'none';
                content.parentElement.classList.remove('active');
            }
        });

        // Toggle untuk dropdown yang diklik
        card.classList.toggle('active');
        dropdown.style.display = card.classList.contains('active') ? 'block' : 'none';
    }
});