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
		handleVote('dog');
	} else {
		window.location.href = 'result.html'
	}
});
//localhost
function handleVote(option) {
	fetch('http://localhost:6110/vote', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({option}),
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not oks');
		}
		return response.json();
	})
	.then(data => {
		console.log('new vote:', data);
		fetchResults();
		// alert(`你投票选择了: ${data.option}。总投票数: ${data.count}`);;
	})
	.catch((error) => {
		console.error('error:', error);
	});
}
