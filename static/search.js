$(document).ready(function () {
  $("#search-form").submit(function (event) {
    var searchInput = $("#search-input").val().trim();
    if (searchInput === "") {
      event.preventDefault(); // Prevent form submission
      $("#search-input").focus();
      $("#search-input").val("");
    }
  });

  $(".word-search").click(function () {
    // Get the text of the clicked word
    var searchText = $(this).text().trim();
    // Set the search input value to the clicked word
    $("#search-input").val(searchText);
    // Submit the form
    $("#search-form").submit();
  });
});
