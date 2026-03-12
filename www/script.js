document.addEventListener('DOMContentLoaded', function() {
    const clickBtn = document.getElementById('clickBtn');
    const message = document.getElementById('message');
    
    let clickCount = 0;
    
    clickBtn.addEventListener('click', function() {
        clickCount++;
        message.textContent = `你点击了按钮 ${clickCount} 次！JavaScript 工作正常！`;
        message.classList.add('show');
        
        // 添加简单的动画效果
        message.style.opacity = '0';
        setTimeout(() => {
            message.style.transition = 'opacity 0.3s';
            message.style.opacity = '1';
        }, 10);
    });
    
    console.log('HTML Lab 已加载完成！');
    console.log('支持的功能：HTML, CSS, JavaScript');
});
