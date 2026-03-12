$(document).ready(function() {
    let clickCount = 0;
    
    // Click button handler
    $('#clickBtn').on('click', function() {
        clickCount++;
        
        // Show spinner
        $('#btnSpinner').removeClass('d-none');
        
        // Simulate async operation
        setTimeout(function() {
            // Hide spinner
            $('#btnSpinner').addClass('d-none');
            
            // Show message using Bootstrap alert
            const $message = $('#message');
            $message.removeClass('d-none alert-info alert-success');
            $message.addClass('alert-success');
            $message.html(`<strong>成功！</strong> 你点击了按钮 <span class="badge bg-primary">${clickCount}</span> 次！jQuery 和 Bootstrap 工作正常！`);
            
            // Auto hide after 3 seconds
            setTimeout(function() {
                $message.addClass('d-none');
            }, 3000);
        }, 500);
    });
    
    // Tooltip initialization
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Console logs
    console.log('HTML Lab 已加载完成！');
    console.log('技术栈：Django 5 + Bootstrap 5 + jQuery');
    console.log('Bootstrap 版本:', bootstrap.Tooltip.VERSION);
    console.log('jQuery 版本:', $.fn.jquery);
});
