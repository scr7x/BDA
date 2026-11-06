use("admin");

use("ecommerce");

// db.reviews.insertMany([
//     {name: "A", pid: "P101", category: "Electronics", rating: "4", comment: "Good read", review_date: ISODate("2026-09-01")},
//     {name: "B", pid: "P101", category: "Electronics", rating: "5", comment: "Excellent product", review_date: ISODate("2026-09-02")},
//     {name: "C", pid: "P102", category: "Books", rating: "3", comment: "slow shipping", review_date: ISODate("2026-09-03")},
//     {name: "D", pid: "P103", category: "Clothing", rating: "2", comment: "Poor quaility", review_date: ISODate("2026-09-04")},
//     {name: "E", pid: "P102", category: "Books", rating: "4", comment: "Good read", review_date: ISODate("2026-09-05")},
// ])

// db.reviews.find();

// db.reviews.aggregate([
//     {$group: {_id: "$pid", total_reviews: {$sum: 1}}}
// ])

// db.reviews.aggregate([
//     {$group: {_id: "$pid", average_rating: {$avg: "$rating"}}},
//     {$sort:{average_rating: -1}}
// ])

// db.reviews.aggregate([
//     {$group: {_id: "$pid", total_reviews:{$sum: 1}}},
//     {$sort: {total_reviews: -1}},
//     {$limit: 5}
// ])

db.reviews.aggregate([
    {$group: {_id: "$category", average_rating: {$avg: "$rating"}}}
])
