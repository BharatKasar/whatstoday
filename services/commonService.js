class CommonService {
    constructor() {}

    canDo = (day) => {
        // Phase 1: first 7 days
        if (day < 7) return true;

        // Phase 2: next 13 days (7 trues alternating)
        if (day < 20) {
            return (day - 7) % 2 === 0;
        }

        // Phase 3+: expanding intervals
        let remaining = day - 20;
        let gap = 3;

        while (true) {
            // gap-1 false days
            if (remaining < gap - 1) return false;

            remaining -= gap - 1;

            // true day
            if (remaining === 0) return true;

            remaining -= 1;

            // increase interval
            gap++;
        }
    }


    canDoFromDate = (startDate, today = new Date()) =>{
        if (!startDate) startDate = "2026-01-26";
        const DAY = 86400000;
        const diff = Math.floor((today - new Date(startDate)) / DAY);

        if (diff < 0) return false;

        return this.canDo(diff);
    }

}


module.exports = new CommonService();