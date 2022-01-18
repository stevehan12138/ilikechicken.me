document.addEventListener('DOMContentLoaded', () => {
    const startedDate = new Date(2021, 3, 10);
    const now = new Date();
    const diff = now.getTime() - startedDate.getTime()

    let timeE = document.getElementById('time');
    timeE.innerHTML = "Months website is up: " + Math.floor(diff / (1000*60*60*24)) + " days since 2021/3/10";

    $('#banner').on('inview', function(event, isInView) {
        if (isInView) {
            $('#banner').removeClass( "hidden");
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
            $('.introduction').removeClass( "hidden");
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

    $('.exp').on('inview', function(event, isInView) {
        if (isInView) {
            $('.exp').removeClass( "hidden");
            anime({
                targets: '.exp',
                easing: 'easeOutQuart',
                translateX: [100, 0],
                opacity: [0, 1],
                duration: 1200,
            })
            $('.exp').off('inview');
        }
    })

    $('.skill').on('inview', function(event, isInView) {
        if (isInView) {
            $('.skill').removeClass( "hidden");
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

    $('.hobbie').on('inview', function(event, isInView) {
        if (isInView) {
            $('.hobbie').removeClass( "hidden");
            anime({
                targets: '.hobbie',
                easing: 'easeOutQuart',
                translateX: [-100, 0],
                opacity: [0, 1],
                duration: 800,
            })
            $('.hobbie').off('inview');
        }
    })
})