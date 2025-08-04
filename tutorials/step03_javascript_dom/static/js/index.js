/**
 * index.js - ToDoリスト（メインページ）専用JavaScript
 * 完了切り替え機能とメッセージ表示機能
 */

// ページ読み込み完了時に実行
document.addEventListener('DOMContentLoaded', function() {
    console.log('📝 ToDoリストページのJavaScript機能を初期化中...');
    
    // 完了切り替えボタンの機能を初期化
    initializeTodoToggleButtons();
});

/**
 * 完了切り替えボタンの初期化
 */
function initializeTodoToggleButtons() {
    document.querySelectorAll('.todo-toggle-btn').forEach(button => {
        button.addEventListener('click', function() {
            const todoId = this.getAttribute('data-todo-id');
            const todoCard = this.closest('.todo-card');
            
            // サーバーに完了状態切り替えのリクエスト送信
            fetch(`/api/toggle-todo/${todoId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // UI を更新
                    updateTodoCardUI(todoCard, data.completed, this);
                    
                    // 成功メッセージ表示
                    showMessage(data.message, 'success');
                    console.log('✅ タスクの状態を更新しました:', data.message);
                } else {
                    showMessage('エラーが発生しました', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showMessage('通信エラーが発生しました', 'error');
            });
        });
    });
}

/**
 * ToDoカードのUI更新
 */
function updateTodoCardUI(todoCard, completed, toggleButton) {
    if (completed) {
        // 完了状態にする
        todoCard.classList.remove('pending');
        todoCard.classList.add('completed');
        toggleButton.textContent = '↩️ 未完了にする';
        todoCard.querySelector('.status-icon').textContent = '✅';
        todoCard.querySelector('.status-text').textContent = '完了';
    } else {
        // 未完了状態にする
        todoCard.classList.remove('completed');
        todoCard.classList.add('pending');
        toggleButton.textContent = '✅ 完了にする';
        todoCard.querySelector('.status-icon').textContent = '⏰';
        todoCard.querySelector('.status-text').textContent = '未完了';
    }
}

/**
 * メッセージ表示機能
 */
function showMessage(message, type) {
    const messageArea = document.getElementById('js-message-area');
    const messageText = document.getElementById('js-message-text');
    
    if (messageArea && messageText) {
        messageText.textContent = message;
        messageArea.className = `js-message-area alert alert-${type === 'success' ? 'success' : 'danger'}`;
        messageArea.style.display = 'block';
        
        // 3秒後に自動で非表示
        setTimeout(() => {
            messageArea.style.display = 'none';
        }, 3000);
    }
}