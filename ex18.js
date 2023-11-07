const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2

};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];


function calculatePointsForDay(jellyfishDay) {
    let dayPoints = 0;
    
    for (const jellyfish of jellyfishDay) {
        const species = identifySpecies(jellyfish);
        const points = speciesPoints[species] || 1;
        dayPoints += points;
        console.log(`SpongeBob Caught a ${species} jellyfish!`);
        console.log(`Patrick identified a ${species} jellyfish!`)
        console.log( `Score: ${dayPoints} points.`)
    }
    return dayPoints;
}




function identifySpecies(jellyfish) {
    const color = jellyfish.color;
    switch (color) {
        case 'pink':
            return 'pink spotted';
        case 'blue':
            return 'blue stinger';
        case 'green':
            return 'green itches';
        default:
            return 'common';
    }
}

for (let i = 0; i < jellyfishDays.length; i++) {
    const dayPoints = calculatePointsForDay(jellyfishDays[i]);
    console.log(`end of the day ,Total points for day ${i + 1}: ${dayPoints}`);
}

// Display the overall total points at the end of the adventure
let totalPoints = 0;
for (const jellyfishDay of jellyfishDays) {
    totalPoints += calculatePointsForDay(jellyfishDay);
}
console.log(`End of the adventure. Total points earned: ${totalPoints}`);
