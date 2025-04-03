function enter_your_email() {
    const email_field = document.getElementById("email_field");
    const yes_email = document.getElementById("yes_email");
    
    if (yes_email.checked) {
        email_field.style.display = "block"; // let the user fill his email
    } else {
        email_field.style.display = "none"; // do not let the user fill his email
    }
}

function preferred_video_way(){
    const pref_video_way = document.getElementById("pref_video_way");
    const yes_video = document.getElementById("yes_video");
    console.log("preferred_video_way is called");
    if (yes_video.checked){
        pref_video_way.style.display = "block"; // let the user choose his preferred way 
    } else {
        pref_video_way.style.display = "none"; // do not let the user choose his preferred way 
    }
}

function validateForm() {
    const email = document.getElementById("email").value;

    const phone_number = document.getElementById("phone_number").value;
    const valid_form_number1 = /^\+[0-9]{10}$/; 
    const valid_form_number2 = /^[0-9]{10}$/;

    const password = document.getElementById("password").value;
    const confirm_password = document.getElementById("confirm_password").value;
    const password_pattern= /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+={}[\]:;,.<>?/-]).{8,}/;

    if (document.getElementById("yes_email").checked) {

        if (!email.includes('@')) {
            alert("Please enter a valid email.");
            return false;
        }
    }

    if (!valid_form_number1.test(phone_number) && !valid_form_number2.test(phone_number)) {
        alert("Please enter a valid phone number.");
        return false;
    }

    if (password != confirm_password) {
        alert("passwords do not match! try again.");
        return false;
    }

    if (!password_pattern.test(password)) {
        alert("Please enter a valid password");
        return false;
    }
    
    return true;
}

function goBack(){
    window.location.href = "/";
}