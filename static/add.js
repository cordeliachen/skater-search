$(document).ready(function () {
  $("#submit-btn").click(function () {
    var new_skater = checkAllFields();
    if (new_skater) {
      save_skater(new_skater);
    }
  });

  $("#edit-btn").click(function () {
    var new_skater = checkAllFields();
    if (new_skater) {
      new_skater.id = id;
      edit_skater(new_skater);
    }
  });

  $("#discard-btn").click(function () {
    // Show a confirmation dialog
    var isConfirmed = confirm("Are you sure you want to discard changes?");

    // If user confirms, redirect to the view page
    if (isConfirmed) {
      window.location.href = "/view/" + id;
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
        $("#birthday-month").val("");
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

  function edit_skater(new_skater) {
    $.ajax({
      type: "POST",
      url: "edit_skater",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(new_skater),
      success: function (id) {
        window.location.href = "/view/" + id.id;
      },
      error: function (request, status, error) {
        console.log("Error");
        console.log(request);
        console.log(status);
        console.log(error);
      },
    });
  }

  function checkAllFields() {
    // Retrieve values from input fields
    var name = $("#name").val().trim();
    var image = $("#image").val().trim();
    var country = $("#country").val().trim();
    var discipline = $("#discipline").val().trim();
    var coach = $("#coach").val().trim();
    var began_skating = parseInt($("#began_skating").val().trim());
    var age = parseInt($("#age").val().trim());
    var birthdayMonth = $("#birthday-month").val();
    var birthdayDay = parseInt($("#birthday-day").val().trim());
    var birthdayYear = parseInt($("#birthday-year").val().trim());
    var birthplace = $("#birthplace").val().trim();

    // Check for empty fields or invalid input
    var isNameValid = isNameOk(name);
    var isImageValid = isImageOk(image);
    var isCountryValid = isCountryOk(country);
    var isDisciplineValid = isDisciplineOk(discipline);
    var isCoachValid = isCoachOk(coach);
    var isBeganSkatingValid = isBeganSkatingOk(began_skating);
    var isAgeValid = isAgeOk(age);
    var isBirthdayValid = isBirthdayOk(
      birthdayMonth,
      birthdayDay,
      birthdayYear
    );
    var isBirthplaceValid = isBirthplaceOk(birthplace);

    // Return false if any check fails
    if (
      !isNameValid ||
      !isImageValid ||
      !isCountryValid ||
      !isDisciplineValid ||
      !isCoachValid ||
      !isBeganSkatingValid ||
      !isAgeValid ||
      !isBirthdayValid ||
      !isBirthplaceValid
    ) {
      return false;
    } else {
      // Return new skater object
      var new_skater = {
        name: name,
        image: image,
        country: country,
        discipline: discipline,
        coach: coach,
        began_skating: began_skating,
        age: age,
        birthday: birthdayMonth + " " + birthdayDay + ", " + birthdayYear,
        birthplace: birthplace,
        results: {},
      };
      return new_skater;
    }
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
    if (isNaN(began_skating) || began_skating < 1990 || began_skating > 2024) {
      $("#began-skating-error").text("Began skating year is invalid").show();
      return false;
    } else {
      $("#began-skating-error").hide();
      return true;
    }
  }

  function isAgeOk(age) {
    if (isNaN(age) || age < 1 || age > 100) {
      $("#age-error").text("Age is invalid").show();
      return false;
    } else {
      $("#age-error").hide();
      return true;
    }
  }

  function isBirthdayOk(birthdayMonth, birthdayDay, birthdayYear) {
    if (!birthdayMonth) {
      $("#birthday-error").text("Birth month is required").show();
      return false;
    } else if (isNaN(birthdayDay) || birthdayDay < 1 || birthdayDay > 31) {
      $("#birthday-error").text("Birthday day is invalid").show();
      return false;
    } else if (
      isNaN(birthdayYear) ||
      birthdayYear < 1900 ||
      birthdayYear > new Date().getFullYear()
    ) {
      $("#birthday-error").text("Birthday year is invalid").show();
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
