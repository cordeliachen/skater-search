$(document).ready(function () {
  $("#submit-btn").click(function () {
    // Retrieve values from input fields
    var name = $("#name").val().trim();
    var image = $("#image").val().trim();
    var country = $("#country").val().trim();
    var discipline = $("#discipline").val().trim();
    var coach = $("#coach").val().trim();
    var began_skating = parseInt($("#began_skating").val().trim());
    var age = parseInt($("#age").val().trim());
    var birthday = $("#birthday").val().trim();
    var birthplace = $("#birthplace").val().trim();

    // Check for empty fields or invalid input
    var isNameValid = isNameOk(name);
    var isImageValid = isImageOk(image);
    var isCountryValid = isCountryOk(country);
    var isDisciplineValid = isDisciplineOk(discipline);
    var isCoachValid = isCoachOk(coach);
    var isBeganSkatingValid = isBeganSkatingOk(began_skating);
    var isAgeValid = isAgeOk(age);
    var isBirthdayValid = isBirthdayOk(birthday);
    var isBirthplaceValid = isBirthplaceOk(birthplace);

    // Check if all fields are valid before proceeding
    if (
      isNameValid &&
      isImageValid &&
      isCountryValid &&
      isDisciplineValid &&
      isCoachValid &&
      isBeganSkatingValid &&
      isAgeValid &&
      isBirthdayValid &&
      isBirthplaceValid
    ) {
      // Create new skater object
      var new_skater = {
        name: name,
        image: image,
        country: country,
        discipline: discipline,
        coach: coach,
        began_skating: began_skating,
        age: age,
        birthday: birthday,
        birthplace: birthplace,
        results: {},
      };

      // Call save_skater function
      save_skater(new_skater);
    }
  });

  function save_skater(new_skater) {
    $.ajax({
      type: "POST",
      url: "save_skater",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(new_skater),
      success: function (id) {
        $("input[type='text']").val("");
        $("input[type='number']").val("");
        $("#name").focus();

        $("#success-message")
          .text("New item successfully created.")
          .append(
            '<a class="btn accent white-txt txt" id="see-it-btn" href="/view/' +
              id.id +
              '">See it here</a>'
          );
      },
      error: function (request, status, error) {
        console.log("Error");
        console.log(request);
        console.log(status);
        console.log(error);
      },
    });
  }

  function isNameOk(name) {
    if (name.trim() === "") {
      $("#name-error").text("Name is required").show();
      return false;
    } else {
      $("#name-error").hide();
      return true;
    }
  }

  function isImageOk(image) {
    if (image.trim() === "") {
      $("#image-error").text("Image URL is required").show();
      return false;
    } else {
      $("#image-error").hide();
      return true;
    }
  }

  function isCountryOk(country) {
    if (country.trim() === "") {
      $("#country-error").text("Country is required").show();
      return false;
    } else {
      $("#country-error").hide();
      return true;
    }
  }

  function isDisciplineOk(discipline) {
    if (discipline.trim() === "") {
      $("#discipline-error").text("Discipline is required").show();
      return false;
    } else {
      $("#discipline-error").hide();
      return true;
    }
  }

  function isCoachOk(coach) {
    if (coach.trim() === "") {
      $("#coach-error").text("Coach is required").show();
      return false;
    } else {
      $("#coach-error").hide();
      return true;
    }
  }

  function isBeganSkatingOk(began_skating) {
    if (isNaN(began_skating)) {
      $("#began-skating-error").text("Began skating must be a number").show();
      return false;
    } else {
      $("#began-skating-error").hide();
      return true;
    }
  }

  function isAgeOk(age) {
    if (isNaN(age)) {
      $("#age-error").text("Age must be a number").show();
      return false;
    } else {
      $("#age-error").hide();
      return true;
    }
  }

  function isBirthdayOk(birthday) {
    if (birthday.trim() === "") {
      $("#birthday-error").text("Birthday is required").show();
      return false;
    } else {
      $("#birthday-error").hide();
      return true;
    }
  }

  function isBirthplaceOk(birthplace) {
    if (birthplace.trim() === "") {
      $("#birthplace-error").text("Birthplace is required").show();
      return false;
    } else {
      $("#birthplace-error").hide();
      return true;
    }
  }
});
