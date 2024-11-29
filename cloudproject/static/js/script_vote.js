
catSelected=false
document.getElementById('catButton').addEventListener('click', function() {
	if (!catSelected) {
		document.querySelector('h1').innerText = '🐱\nYou chose cats!';
		this.innerText = 'click to view the results';
		document.getElementById('dogButton').style.display = 'none';
	    catSelected = true; // 标记为已选择猫
		handleVote('cat');
	} else {
	    // 第二次点击猫按钮时跳转
	    window.location.href = 'result.html';
	}
});

dogSelected=false
document.getElementById('dogButton').addEventListener('click', function() {
    if (!dogSelected) {
		document.querySelector('h1').innerText = '🐶\nYou chose Dogs!';
		this.innerText = 'click to view the results';
		document.getElementById('catButton').style.display = 'none';
		dogSelected=true;
		handleVoted('dog');
	} else {
		window.location.href = 'result.html'
	}
});

// function handleVote(option) {
// 	fetch('http://localhost:6110/vote', {
// 		method: 'POST',
// 		headers: {
// 			'Content-Type': 'application/json',
// 		},
// 		body: JSON.stringify({ option }),
// 	})
// 	.then(response => {
// 		if (!response.ok) {
// 			throw new Error('Network response was not ook');
// 		}
// 		return response.json();
// 	})
// 	.then(data => {
// 		console.log('new vote:', data);
// 		fetchResults();
// 		// alert(`你投票选择了: ${data.option}。总投票数: ${data.count}`);
// 	})
// 	.catch((error) => {
// 		console.error('error:', error);
// 	});
// }

// function handleVote(option) {
//   var xhr = new XMLHttpRequest();  // 创建 XMLHttpRequest 对象
//   xhr.open('POST', 'http://localhost:6110/vote', true);  // 初始化请求
//
//   xhr.setRequestHeader('Content-Type', 'application/json');  // 设置请求头
//
//   // 监听请求的状态变化
//   xhr.onload = function () {
//     if (xhr.status >= 200 && xhr.status < 300) {
//       try {
//         var data = JSON.parse(xhr.responseText);  // 解析返回的 JSON 数据
//         console.log('new vote:', data);
//         fetchResults();  // 获取最新的投票结果
//       } catch (error) {
//         console.error('Error parsing response:', error);
//       }
//     } else {
//       console.error('Request failed with status:', xhr.status);
//     }
//   };
//
//   // 监听请求错误
//   xhr.onerror = function () {
//     console.error('Request failed due to network error');
//   };
//
//   // 发送请求
//   var payload = JSON.stringify({ option: option });
//   xhr.send(payload);
// }


