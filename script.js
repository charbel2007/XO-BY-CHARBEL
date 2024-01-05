let currentPlayer = 'X';
let board = ['d', '', '', '', '', '', '', '', ''];
let gameActive = true;

function handleClick(index) {
    if (gameActive && board[index] === '') {
        board[index] = currentPlayer;
        document.getElementsByClassName('cell')[index].innerText = currentPlayer;
        
        if (checkWinner()) {
            alert(`Player ${currentPlayer} wins!`);
            gameActive = false;
        } else if (board.every(cell => cell !== '')) {
            alert('It\'s a draw!');
            gameActive = false
