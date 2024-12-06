/**Открытие полного описания товара */
document.addEventListener("DOMContentLoaded", () => {
  const readMoreLinks = document.querySelectorAll(".read-more-link");

  readMoreLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault(); // Предотвращаем стандартное поведение ссылки

      // Ищем ближайшее модальное окно к карточке, на которой был клик
      const modal = link.closest(".card-body").querySelector(".modal");

      if (modal) {
        modal.classList.add("visible");

        // Инициализируем карусель (если она есть) и запускаем автопрокрутку
        const carousel = modal.querySelector(".carousel");
        if (carousel) {
          // Проверяем, есть ли уже инициализированная карусель, если нет - инициализируем
          const bsCarousel =
            bootstrap.Carousel.getInstance(carousel) ||
            new bootstrap.Carousel(carousel);
          bsCarousel.cycle(); // Запуск автопрокрутки
        }
      }
    });
  });

  const closeButtons = document.querySelectorAll(".close-btn");

  closeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const modal = btn.closest(".modal");
      if (modal) {
        modal.classList.remove("visible"); // Закрытие модального окна
      }
    });
  });

  // Закрытие модального окна, если кликнули вне его
  const modals = document.querySelectorAll(".modal");
  modals.forEach((modal) => {
    modal.addEventListener("click", (e) => {
      // Закрытие модального окна при клике по фону
      if (e.target === modal) {
        modal.classList.remove("visible");
      }
    });
  });
});

/**Открытие карточек */
document.addEventListener("DOMContentLoaded", () => {
  const row = document.querySelector(".ground"); // Контейнер для карточек

  // Запускаем анимацию для всего контейнера
  setTimeout(() => {
    row.classList.add("appear"); // Добавляем класс для появления карточек
  }, 100); // Задержка появления контейнера
});
