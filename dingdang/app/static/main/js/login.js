var pwd = document.getElementById('pwd');
var email = document.getElementById('email');
var id;
var submit = document.getElementById('submit');
submit.addEventListener('click', function() {
    fetch("http://120.24.4.254:5455/api/login/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email.value,
            password: pwd.value
        })
    }).then(res => {
        if (res.ok)
            return res.json()
        else
            console.log("error");
    }).then(value => {
        cookie.setCookie("id", value.user_id)
        id = value.user_id
        console.log("id = ", id)
        window.location = "http://120.24.4.254:5455/main/"
    })
})