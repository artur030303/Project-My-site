/**полное описания товара */
document.addEventListener("DOMContentLoaded", () => {
  const readMoreLinks = document.querySelectorAll(".read-more-link");

  readMoreLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      // ищем ближайшее модальное окно к карточке, на которой был клик
      const modal = link.closest(".card-body").querySelector(".modal");
      if (modal) {
        modal.classList.add("visible");

        // инициализируем карусель
        const carousel = modal.querySelector(".carousel");
        if (carousel) {
          const bsCarousel =
            bootstrap.Carousel.getInstance(carousel) ||
            new bootstrap.Carousel(carousel);
          bsCarousel.cycle(); // Запуск автопрокрутки
        }
      }
    });
  });

  /** закрытие модального окна*/
  const closeButtons = document.querySelectorAll(".close-btn");

  closeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const modal = btn.closest(".modal");
      if (modal) {
        modal.classList.remove("visible");
      }
    });
  });

  // закрытие модального окна при клике по фону
  const modals = document.querySelectorAll(".modal");
  modals.forEach((modal) => {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.classList.remove("visible");
      }
    });
  });
});

/**открытие карточек */
document.addEventListener("DOMContentLoaded", () => {
  const row = document.querySelector(".ground");

  // запускаем анимацию для всего контейнера
  setTimeout(() => {
    row.classList.add("appear");
  }, 100);
});

//**открытие корзины (значок) */
document.addEventListener("DOMContentLoaded", function () {
  const modalButton = document.getElementById("modalButton");
  const includedBasket = document.getElementById("includedBasket");

  // Показать корзину при нажатии на кнопку
  modalButton.addEventListener("click", function () {
    includedBasket.style.display = "flex"; // Показываем корзину
  });

  // Закрытие корзины при клике на фон (внешнюю часть модального окна)
  includedBasket.addEventListener("click", function (e) {
    if (e.target === includedBasket) {
      includedBasket.style.display = "none"; // Скрываем корзину
    }
  });
});
