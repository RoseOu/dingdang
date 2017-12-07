
var pwd = document.getElementById('pwd');
var email = document.getElementById('email');
var username = document.getElementById('username');
var id;
var submit = document.getElementById('submit');
submit.addEventListener('click', function() {
    fetch("http://120.24.4.254:5455/api/register/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email.value,
            password: pwd.value,
            username: username.value
        })
    }).then(res => {
        if (res.ok)
            return res.json()
        else
            console.log("error");
    }).then(value => {
        window.location = "http://120.24.4.254:5455/main/login/"
    })
})