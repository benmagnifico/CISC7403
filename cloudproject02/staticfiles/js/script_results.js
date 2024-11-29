// 返回按钮事件
show();
document.getElementById('backButton').addEventListener('click',  function(){
	// window.location.href = 'vote.html'; // 返回投票页面的路径
});

function show() {
	$.ajax({
		url: 'http://localhost:6111/result/',//这个地方更换为服务器端api路径
		type: 'GET',
		dataType: 'json',
		success: function(response) {
			//const jsonData = {
			//	"catVote":10,
			//	"dogVote":20,
			//	"catperc":"33.3%",//百分比数据换成字符串再传入
			//	"dogperc":"66.7%",
			//	"totalVote":30
			//};//一个测试的例子，在error情况下已经跑通
			let jsonData = JSON.parse(response);//以json数据传输内容：样例应如
			//{'catVote':10,'dogVote':20,'catperc':'33.3%','dogperc':'66.7%'，'totalVote':30}，用这个方法解析
			$('.vote-count-cats').text(`Cats: ${jsonData.catVote} vote`);//catVote是数据中对应的选择猫的票数信息
			$('.cat-percentage').text(`${jsonData.catperc}`);//catperc是数据中对应的选择猫的占比信息
			$('.vote-count-dogs').text(`Dogs: ${jsonData.dogVote} vote`);//dogVote是数据中对应的选择狗的票数信息
			$('.dog-percentage').text(`${jsonData.dogperc}`);//dogperc是数据中对应的选择狗的占比信息
			$('.vote-count-total').text(`total: ${jsonData.totalVote} vote`);//对应投票总数
		},
		error: function(xhr, errmsg, err) {
			//const jsonData = {
			//	"catVote":10,
			//	"dogVote":20,
			//	"catperc":"33.3%",
			//	"dogperc":"66.7%",
			//	"totalVote":30
			//};
			//$('.vote-count-cats').text(`Cats: ${jsonData.catVote} vote`);//catVote是数据中对应的选择猫的票数信息
			//$('.cat-percentage').text(`${jsonData.catperc}`);//catperc是数据中对应的选择猫的占比信息
			//$('.vote-count-dogs').text(`Dogs: ${jsonData.dogVote} vote`);//dogVote是数据中对应的选择狗的票数信息
			//$('.dog-percentage').text(`${jsonData.dogperc}`);//dogperc是数据中对应的选择狗的占比信息
			//$('.vote-count-total').text(`total: ${jsonData.dogVote} vote`);//对应投票总数
			$('h1').text('👀 Oops, An error occurred!');
			$('.container > *').not('h1').not('#backButton').hide();		
		}

	});
}