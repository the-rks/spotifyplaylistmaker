// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQBsO5l0BHwRzCzOCIQ5_Ujb-mLXw2tX8bnMnDjGv-CGRyZBlD1q4eVzvLgxTSwQzShI6lAHDVwwuoQOQd7Nbyp8RB6PcWYOSz4gPakqnDA2bBUKTjwTygdMLHVvoZpd5ubYXFAkWYkbhskFH66vJJnoPvfvmEtc_tOMaXOxZoPDIfAb-J7yZOt3_hNdzXscXdi2ll-R7CdZgX9pIqhpjvTj0iEhryZM6PnGME0o42xCBRaMqkleiqo1bPQz_nYBrUnrF7tz0mID3p0dPXb_e3RlpJPfLbjC';
async function fetchWebApi(endpoint, method, body) {
    const res = await fetch(`https://api.spotify.com/${endpoint}`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
        method,
        body: JSON.stringify(body)
    });
    return await res.json();
}

async function getTopTracks() {
    // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    return (await fetchWebApi(
        'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
    )).items;
}

const topTracks = await getTopTracks();
console.log(
    topTracks?.map(
        ({ name, artists }) =>
            `${name} by ${artists.map(artist => artist.name).join(', ')}`
    )
);