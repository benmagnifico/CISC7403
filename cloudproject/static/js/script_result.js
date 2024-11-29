// 返回按钮事件
document.getElementById('backButton').addEventListener('click',  function(){
	window.location.href = 'vote.html'; // 返回投票页面的路径
});
// 获取投票结果
function fetchResults() {
	fetch('http://localhost:6111/results')
		.then(response => response.json())
		.then(data => {
			const resultsDiv = document.getElementById('results');
			resultsDiv.innerHTML = ''; // 清空之前的结果
			data.forEach(vote => {
				document.getElementsByClassName('cat-percentage')textContent=${vote.option}
				document.getElementsByClassName('dog-percentage')textContent=${vote.option}
				document.getElementsByClassName('vote-count-cats')textContent=${vote.option}
				document.getElementsByClassName('vote-count-dogs')textContent=${vote.option}
				document.getElementsByClassName('vote-count-total')textContent=${vote.option}
			});
		})
		.catch((error) => {
			console.error('error:', error);
		});
}

// 加载结果
fetchResults();


