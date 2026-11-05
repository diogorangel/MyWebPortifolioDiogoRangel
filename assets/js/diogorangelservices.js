const menuButton =
    document.querySelector(".menu-button"); const nav = document.querySelector(".nav"); const filters =
        document.querySelectorAll(".filter"); const cards = document.querySelectorAll(".service-card"); const detailsButtons =
            document.querySelectorAll(".details-button"); menuButton.addEventListener("click", () => {
                nav.classList.toggle("open");
            }); document.querySelectorAll(".nav a").forEach((link) => {
                link.addEventListener("click", () => {
                    nav.classList.remove("open");
                });
            }); filters.forEach((filter) => {
                filter.addEventListener("click", () => {
                    filters.forEach((button) => button.classList.remove("active")); filter.classList.add("active"); const selectedCategory =
                        filter.dataset.filter; cards.forEach((card) => {
                            const cardCategory = card.dataset.category; const showCard =
                                selectedCategory === "todos" || selectedCategory === cardCategory; card.style.display = showCard ? "block" : "none";
                        });
                });
            }); detailsButtons.forEach((button) => {
                button.addEventListener("click", () => {
                    const card =
                        button.closest(".service-card"); const isOpen = card.classList.toggle("open"); button.textContent = isOpen ? "Ocultar detalhes −" : "Ver detalhes + "; }); }); document.getElementById("year").textContent = new Date().getFullYear();