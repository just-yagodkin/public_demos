export default function (dt, target = 's  erial', action = 'send') {
    const payload = formatDate(dt);
    const params = {
        detail: {
            target,
            action,
            payload,
        }
    };
    const event = new CustomEvent('jspsych', params);
    document.dispatchEvent(event);
}

function formatDate(date) {
    return `${date.getDay()}-${date.getMonth()}-${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}.${date.getMilliseconds()}`;
}
