/**
 * main.js - 共通JavaScript機能
 * DOM操作、イベント処理、学習用インタラクティブ機能
 */

// ========================================
// 1. DOMContentLoadedイベント（ページ読み込み完了時に実行）
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    console.log('📚 Step 3: JavaScript DOM操作が開始されました');
    
    // DOM操作機能を初期化
    initializeDOMFunctions();
    initializeEventListeners();
    initializeInteractiveFunctions();
    
    console.log('✅ すべてのJavaScript機能が準備完了しました');
});

// ========================================
// 2. 基本的なDOM操作機能
// ========================================
function initializeDOMFunctions() {
    console.log('🔧 DOM操作機能を初期化中...');
    
    // 「完了済み」「未完了」ボタンを有効化
    enableFilterButtons();
    
    // タスクカードの操作ボタンを有効化
    enableTaskButtons();
    
    // 学習用機能ボタンを追加
    addLearningButtons();
}

// ========================================
// 3. イベントリスナーの設定
// ========================================
function initializeEventListeners() {
    console.log('👂 イベントリスナーを設定中...');
    
    // フィルターボタンのイベント設定
    setupFilterButtons();
    
    // タスク操作ボタンのイベント設定
    setupTaskButtons();
}

// ========================================
// 4. フィルター機能（完了済み・未完了の表示切り替え）
// ========================================
function enableFilterButtons() {
    // フィルターボタンエリアを作成
    const sectionHeader = document.querySelector('.section-header');
    if (sectionHeader) {
        const filterButtonsHtml = `
            <div class="filter-buttons" style="margin-top: 15px;">
                <button id="showAll" class="btn btn-secondary">
                    📋 すべて表示
                </button>
                <button id="showCompleted" class="btn btn-success">
                    ✅ 完了済みのみ
                </button>
                <button id="showPending" class="btn btn-warning">
                    ⏰ 未完了のみ
                </button>
            </div>
        `;
        sectionHeader.insertAdjacentHTML('beforeend', filterButtonsHtml);
    }
}

function setupFilterButtons() {
    // すべて表示
    document.getElementById('showAll')?.addEventListener('click', function() {
        showAllTodos();
        updateActiveFilter(this);
    });
    
    // 完了済みのみ表示
    document.getElementById('showCompleted')?.addEventListener('click', function() {
        filterTodosByStatus(true);
        updateActiveFilter(this);
    });
    
    // 未完了のみ表示
    document.getElementById('showPending')?.addEventListener('click', function() {
        filterTodosByStatus(false);
        updateActiveFilter(this);
    });
}

function showAllTodos() {
    const todoCards = document.querySelectorAll('.todo-card');
    todoCards.forEach(card => {
        card.style.display = 'block';
        card.style.opacity = '1';
    });
    console.log('📋 すべてのタスクを表示しました');
}

function filterTodosByStatus(completed) {
    const todoCards = document.querySelectorAll('.todo-card');
    
    todoCards.forEach(card => {
        const isCompleted = card.classList.contains('completed');
        
        if (isCompleted === completed) {
            // 表示
            card.style.display = 'block';
            card.style.opacity = '1';
        } else {
            // 非表示
            card.style.display = 'none';
            card.style.opacity = '0.5';
        }
    });
    
    const statusText = completed ? '完了済み' : '未完了';
    console.log(`${statusText}のタスクのみを表示しました`);
}

function updateActiveFilter(activeButton) {
    // すべてのフィルターボタンからactiveクラスを削除
    document.querySelectorAll('.filter-buttons .btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // クリックされたボタンにactiveクラスを追加
    activeButton.classList.add('active');
}

// ========================================
// 5. タスク操作機能
// ========================================
function enableTaskButtons() {
    // 無効化されているボタンを有効化
    const disabledButtons = document.querySelectorAll('.todo-actions .btn[disabled]');
    disabledButtons.forEach(button => {
        button.disabled = false;
        
        // ボタンテキストから「(予定)」部分を削除
        if (button.textContent.includes('(')) {
            const cleanText = button.textContent.split('(')[0].trim();
            button.textContent = cleanText;
        }
    });
}

function setupTaskButtons() {
    // 編集ボタンのイベント設定
    document.querySelectorAll('.todo-edit-btn').forEach(button => {
        button.addEventListener('click', function() {
            const todoCard = this.closest('.todo-card');
            editTodo(todoCard);
        });
    });
    
    // 削除ボタンのイベント設定
    document.querySelectorAll('.todo-delete-btn').forEach(button => {
        button.addEventListener('click', function() {
            const todoCard = this.closest('.todo-card');
            deleteTodo(todoCard);
        });
    });
}

function editTodo(todoCard) {
    const titleElement = todoCard.querySelector('.todo-title');
    const descriptionElement = todoCard.querySelector('.todo-description');
    
    if (titleElement && descriptionElement) {
        const currentTitle = titleElement.textContent;
        const currentDescription = descriptionElement.textContent;
        
        // タイトルを編集可能にする
        titleElement.contentEditable = true;
        titleElement.style.backgroundColor = '#fff3cd';
        titleElement.style.padding = '5px';
        titleElement.style.border = '1px solid #ffeaa7';
        titleElement.focus();
        
        // 保存ボタンを追加
        const saveButton = document.createElement('button');
        saveButton.textContent = '💾 保存';
        saveButton.className = 'btn btn-sm btn-success';
        saveButton.style.marginLeft = '10px';
        
        saveButton.addEventListener('click', function() {
            titleElement.contentEditable = false;
            titleElement.style.backgroundColor = '';
            titleElement.style.padding = '';
            titleElement.style.border = '';
            this.remove();
            
            console.log(`タスクを編集しました: "${currentTitle}" → "${titleElement.textContent}"`);
        });
        
        titleElement.parentNode.appendChild(saveButton);
    }
}

function deleteTodo(todoCard) {
    const titleElement = todoCard.querySelector('.todo-title');
    const todoTitle = titleElement ? titleElement.textContent : 'タスク';
    
    if (confirm(`「${todoTitle}」を削除しますか？`)) {
        // アニメーション効果
        todoCard.style.transition = 'opacity 0.5s, transform 0.5s';
        todoCard.style.opacity = '0';
        todoCard.style.transform = 'translateX(-100%)';
        
        setTimeout(() => {
            todoCard.remove();
            console.log(`タスクを削除しました: "${todoTitle}"`);
        }, 500);
    }
}

// ========================================
// 6. 学習用インタラクティブ機能
// ========================================
function initializeInteractiveFunctions() {
    console.log('🎮 学習用インタラクティブ機能を初期化中...');
    
    // タスクカードクリックで詳細表示
    setupTaskCardClicks();
    
    // キーボードショートカット
    setupKeyboardShortcuts();
    
    // スタイル変更機能
    setupStyleChanger();
}

function addLearningButtons() {
    // 学習セクションに機能ボタンを追加
    const learningSection = document.querySelector('.learning-section');
    if (learningSection) {
        const learningButtonsHtml = `
            <div class="learning-controls" style="margin-top: 20px; text-align: center;">
                <h4>🎮 JavaScriptで試してみよう！</h4>
                <div class="learning-buttons">
                    <button id="changeTheme" class="btn btn-primary">
                        🎨 色を変える
                    </button>
                    <button id="addNewElement" class="btn btn-success">
                        ➕ 要素を追加
                    </button>
                    <button id="animateCards" class="btn btn-warning">
                        ✨ アニメーション
                    </button>
                    <button id="showStats" class="btn btn-info">
                        📊 統計表示
                    </button>
                </div>
            </div>
        `;
        learningSection.insertAdjacentHTML('beforeend', learningButtonsHtml);
        
        // 学習ボタンのイベント設定
        setupLearningButtons();
    }
}

function setupLearningButtons() {
    // テーマ変更
    document.getElementById('changeTheme')?.addEventListener('click', function() {
        changeTheme();
    });
    
    // 要素追加
    document.getElementById('addNewElement')?.addEventListener('click', function() {
        addNewElement();
    });
    
    // アニメーション
    document.getElementById('animateCards')?.addEventListener('click', function() {
        animateCards();
    });
    
    // 統計表示
    document.getElementById('showStats')?.addEventListener('click', function() {
        showDetailedStats();
    });
}

function setupTaskCardClicks() {
    document.querySelectorAll('.todo-card').forEach(card => {
        card.addEventListener('click', function(e) {
            // ボタンクリックの場合は無視
            if (e.target.classList.contains('btn')) return;
            
            // カードの詳細情報をコンソールに表示
            const title = this.querySelector('.todo-title').textContent;
            const description = this.querySelector('.todo-description').textContent;
            console.log(`📋 タスク詳細: ${title} - ${description}`);
            
            // カードをハイライト
            this.style.boxShadow = '0 0 20px rgba(0, 123, 255, 0.5)';
            setTimeout(() => {
                this.style.boxShadow = '';
            }, 1000);
        });
    });
}

function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl + H で健康チェック情報表示
        if (e.ctrlKey && e.key === 'h') {
            e.preventDefault();
            fetch('/health')
                .then(response => response.json())
                .then(data => {
                    alert(`📊 アプリケーション状態:\n${data.message}\nステップ: ${data.step}\n機能: ${data.description}`);
                });
        }
    });
}

function setupStyleChanger() {
    let currentTheme = 0;
    const themes = [
        { name: 'デフォルト', primary: '#007bff', secondary: '#6c757d' },
        { name: 'グリーン', primary: '#28a745', secondary: '#20c997' },
        { name: 'オレンジ', primary: '#fd7e14', secondary: '#ffc107' },
        { name: 'パープル', primary: '#6f42c1', secondary: '#e83e8c' }
    ];
    
    window.changeTheme = function() {
        currentTheme = (currentTheme + 1) % themes.length;
        const theme = themes[currentTheme];
        
        document.documentElement.style.setProperty('--primary-color', theme.primary);
        document.documentElement.style.setProperty('--secondary-color', theme.secondary);
        
        console.log(`🎨 テーマを「${theme.name}」に変更しました`);
    };
}

function addNewElement() {
    const container = document.querySelector('.todos-grid');
    const newCard = document.createElement('div');
    newCard.className = 'todo-card pending';
    newCard.innerHTML = `
        <div class="todo-header">
            <div class="todo-status">
                <span class="status-icon">⚡</span>
                <span class="status-text">新規作成</span>
            </div>
            <div class="todo-priority priority-medium">
                🟡 中優先度
            </div>
        </div>
        <div class="todo-body">
            <h3 class="todo-title">JavaScriptで作成したタスク</h3>
            <p class="todo-description">DOM操作で動的に追加されました！</p>
        </div>
        <div class="todo-footer">
            <div class="todo-date">📅 ${new Date().toLocaleDateString('ja-JP')}</div>
        </div>
    `;
    
    // アニメーション効果で追加
    newCard.style.opacity = '0';
    newCard.style.transform = 'translateY(20px)';
    container.appendChild(newCard);
    
    setTimeout(() => {
        newCard.style.transition = 'opacity 0.5s, transform 0.5s';
        newCard.style.opacity = '1';
        newCard.style.transform = 'translateY(0)';
    }, 100);
    
    console.log('➕ 新しいタスクカードを追加しました');
}

function animateCards() {
    const cards = document.querySelectorAll('.todo-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transform = 'scale(1.05)';
            card.style.transition = 'transform 0.3s';
            
            setTimeout(() => {
                card.style.transform = 'scale(1)';
            }, 300);
        }, index * 100);
    });
    
    console.log('✨ タスクカードをアニメーションしました');
}

function showDetailedStats() {
    const totalCards = document.querySelectorAll('.todo-card').length;
    const completedCards = document.querySelectorAll('.todo-card.completed').length;
    const pendingCards = totalCards - completedCards;
    
    const statsMessage = `
📊 詳細統計情報:
・総タスク数: ${totalCards}
・完了済み: ${completedCards}
・未完了: ${pendingCards}
・完了率: ${Math.round((completedCards / totalCards) * 100)}%
・現在時刻: ${new Date().toLocaleString('ja-JP')}
    `;
    
    alert(statsMessage);
    console.log('📊 統計情報を表示しました');
}

// ========================================
// 7. ユーティリティ関数
// ========================================

// より正確な要素選択のためのヘルパー関数
function selectByText(selector, text) {
    const elements = document.querySelectorAll(selector);
    return Array.from(elements).find(el => el.textContent.includes(text));
}

// ========================================
// 8. コンソール出力による学習サポート
// ========================================
console.log(`
🎓 JavaScript DOM操作 - 学習ガイド
=====================================
このファイルで学習できる内容：

1. DOM要素の選択と操作
   - querySelector() / querySelectorAll()
   - 要素の作成・追加・削除

2. イベント処理
   - addEventListener()
   - クリック・キーボードイベント

3. スタイルの動的変更
   - CSS プロパティの変更
   - アニメーション効果

4. 動的コンテンツ
   - innerHTML / textContent
   - 要素の動的生成

実際に試してみてください！
=====================================
`);