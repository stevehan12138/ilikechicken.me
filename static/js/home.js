document.addEventListener('DOMContentLoaded', () => {
    $('#banner').on('inview', function(event, isInView) {
        if (isInView) {
            anime({
                targets: '#banner',
                easing: 'easeOutSine',
                translateY: [-100, 0],
                opacity: [0, 1],
                duration: 500,
            })
            $('#banner').off('inview');
        }
    })

    $('.introduction').on('inview', function(event, isInView) {
        if (isInView) {
            anime({
                targets: '.introduction',
                easing: 'easeOutQuart',
                translateX: [-100, 0],
                opacity: [0, 1],
                duration: 800,
            })
            $('.introduction').off('inview');
        }
    })

    $('.experiences').on('inview', function(event, isInView) {
        if (isInView) {
            anime({
                targets: '.experiences',
                easing: 'easeOutQuart',
                translateX: [100, 0],
                opacity: [0, 1],
                duration: 1200,
            })
            $('.experiences').off('inview');
        }
    })

    $('.skill').on('inview', function(event, isInView) {
        if (isInView) {
            anime({
                targets: '.skill',
                easing: 'easeInExpo',
                translateY: [60, 0],
                opacity: [0, 1],
                duration: 600,
            })
            $('.skill').off('inview');
        }
    })
})