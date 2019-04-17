"""
{
  filterCards(title: "d", sort: title_asc, first: 10, after: "YXJyYXljb25uZWN0aW9uOjI=") {
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage

    }
    edges {
      node {
        id
        title
        createdAt
      }
    }
  }
}

"""