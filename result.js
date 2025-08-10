function grade(score) {
        if (score >= 90) {
            console.log('"A"');
        }
        else {
            if (score >= 80) {
                console.log('"B"');
            }
            else {
                console.log('"C"');
                console.log(grade(90));
            }
        }
}