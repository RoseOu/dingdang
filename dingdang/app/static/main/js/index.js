var showName = document.getElementById('showName');
var id = cookie.getCookie('id');
// id = 2; //chrome关闭跨域时使用
fetch('http://120.24.4.254:5455/api/profile/' + id).then(function(res){
	return res.json()
}).then(value => {
    console.log(value)
    showName.innerHTML = value.email;
})