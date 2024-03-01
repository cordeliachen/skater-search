$(document).ready(function () {
  $("#search-form").submit(function (event) {
    var searchInput = $("#search-input").val().trim();
    if (searchInput === "") {
      event.preventDefault(); // Prevent form submission
      $("#search-input").focus();
      $("#search-input").val("");
    }
  });
});
