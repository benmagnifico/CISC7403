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
				document.getElementsByClassName('cat-percentage')[0].textContent=${vote.catp};
				document.getElementsByClassName('dog-percentage')[0].textContent=${vote.dogp};
				document.getElementsByClassName('vote-count-cats')[0].textContent=${vote.ccat};
				document.getElementsByClassName('vote-count-dogs')[0].textContent=${vote.cdog};
				document.getElementsByClassName('vote-count-total')[0].textContent=${vote.ctotal};
			});
		})
		.catch((error) => {
			console.error('error:', error);
		});
}

// 加载结果
fetchResults();


