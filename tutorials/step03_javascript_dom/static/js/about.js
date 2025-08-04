/**
 * about.html 専用JavaScript
 * デモボタン機能とJavaScript体験機能
 */

// ページ読み込み完了時に実行
document.addEventListener('DOMContentLoaded', function() {
    console.log('📚 Aboutページ専用のJavaScript機能を初期化中...');
    
    // デモボタンの機能設定
    setupDemoButtons();
});

/**
 * デモボタンの機能設定
 */
function setupDemoButtons() {
    const output = document.getElementById('demoOutput');
    
    if (!output) {
        console.warn('デモ出力エリアが見つかりません');
        return;
    }
    
    // 背景色変更ボタン
    const colorChangeBtn = document.getElementById('demoColorChange');
    if (colorChangeBtn) {
        colorChangeBtn.addEventListener('click', function() {
            changeDemoBackgroundColor(output);
        });
    }
    
    // 要素追加ボタン
    const addElementBtn = document.getElementById('demoAddElement');
    if (addElementBtn) {
        addElementBtn.addEventListener('click', function() {
            addDemoElement(output);
        });
    }
    
    // アニメーション実行ボタン
    const animationBtn = document.getElementById('demoAnimation');
    if (animationBtn) {
        animationBtn.addEventListener('click', function() {
            runDemoAnimation(output);
        });
    }
    
    // 現在時刻表示ボタン
    const timeBtn = document.getElementById('demoCurrentTime');
    if (timeBtn) {
        timeBtn.addEventListener('click', function() {
            showCurrentTime(output);
        });
    }
}

/**
 * 背景色をランダムに変更
 */
function changeDemoBackgroundColor(output) {
    const colors = ['#e3f2fd', '#f3e5f5', '#e8f5e8', '#fff3e0', '#fce4ec'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    
    document.body.style.backgroundColor = randomColor;
    output.innerHTML = `<p>✅ 背景色を <strong>${randomColor}</strong> に変更しました！</p>`;
    
    console.log(`🎨 背景色を ${randomColor} に変更しました`);
}

/**
 * 新しい要素を追加
 */
function addDemoElement(output) {
    const newElement = document.createElement('div');
    newElement.style.cssText = 'padding: 10px; margin: 10px 0; background: #4caf50; color: white; border-radius: 5px;';
    newElement.textContent = `📅 ${new Date().toLocaleString('ja-JP')} に作成された要素`;
    
    output.appendChild(newElement);
    output.scrollTop = output.scrollHeight; // 自動スクロール
    
    console.log('➕ 新しい要素を追加しました');
}

/**
 * アニメーション実行
 */
function runDemoAnimation(output) {
    const demoCard = document.querySelector('.demo-card');
    
    if (demoCard) {
        demoCard.style.transform = 'scale(1.05)';
        demoCard.style.transition = 'transform 0.3s';
        
        setTimeout(() => {
            demoCard.style.transform = 'scale(1)';
        }, 300);
        
        output.innerHTML = '<p>✨ アニメーションを実行しました！カードが少し大きくなったのを確認できますか？</p>';
        console.log('✨ アニメーション効果を実行しました');
    } else {
        output.innerHTML = '<p>❌ アニメーション対象の要素が見つかりませんでした</p>';
    }
}

/**
 * 現在時刻を表示
 */
function showCurrentTime(output) {
    const now = new Date();
    const timeString = now.toLocaleString('ja-JP', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
    
    output.innerHTML = `<p>🕐 現在時刻: <strong>${timeString}</strong></p>`;
    console.log(`🕐 現在時刻を表示: ${timeString}`);
}