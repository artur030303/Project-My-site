document.addEventListener("DOMContentLoaded", function () {
  const notifications = document.querySelectorAll(".alert");

  notifications.forEach(function (notification) {
    setTimeout(function () {
      notification.classList.add("fade");
      setTimeout(function () {
        notification.remove();
      }, 500);
    }, 3000);
  });
});
