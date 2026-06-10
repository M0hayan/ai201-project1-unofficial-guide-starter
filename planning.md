# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

The domain I chose was university dorming. Although there are websites that have information about them, there is no single one spot that easily lets you see the differences and decide which is better so I chose this as the domain to make it easier for incoming students. This information is valuable as it allows incoming students to know which housing would be the best for them.

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Official Housing Homepage | This is the university's official housing webpage with a general overview | https://housing.illinoisstate.edu/|
| 2 | Residence Hall Locations Overview | Contains information about the different housing locations | https://housing.illinoisstate.edu/locations/|
| 3 | Reddit: "An Honest Dorm Review: Watterson Towers" | A reddit forum made by a person giving a review on watterson towers living experience | https://www.reddit.com/r/ilstu/comments/1ddvm9y/an_honest_dorm_review_watterson_towers/|
| 4 |Watterson Towers Official Guide | Official webpage containing information about watterson| https://housing.illinoisstate.edu/locations/watterson/|
| 5 | Reddit: "Pros & Cons of ISU Dorms (A Freshman's Guide)"| forum post evaluating dorms in general for freshman| https://www.reddit.com/r/ilstu/comments/1axc3rq|
| 6 |Hewett-Manchester Official Guide | Official webpage containing information about hewett manchester| https://housing.illinoisstate.edu/locations/hewett-manchester/|
| 7 | Housing Contract Terms & Conditions| Contains the general contract rules| https://housing.illinoisstate.edu/contracts/terms/?utm_source=chatgpt.com|
| 8 | International Student Housing Information| housing information for international students | https://internationalengagement.illinoisstate.edu/student-life/housing|
| 9 | Reddit: "Housing" (discussion of Watterson room sizes and community)| Has student experiences of the community of watterson| https://www.reddit.com/r/ilstu/comments/1brtjw3|
| 10 | Reddit: "Best Dorm?"| Students responses regarding that the best dorm is | https://www.reddit.com/r/ilstu/comments/1dn16ef|
| 11 | Residence Hall Policies PDF| Rules and regulations for living | https://housing.illinoisstate.edu/downloads/about/Residence%20Hall%20Policies.pdf |
| 12 | Reddit: Roomate selection with TLLCs | Has student recoutns on filtering and contacting potential roomates | https://www.reddit.com/r/ilstu/comments/1k8v5bg/roommate_selection_with_tllcs/|
| 13 | Reddit overcrowding | Student discussion about overcrowding in dorms | https://www.reddit.com/r/ilstu/comments/1fyhm3n/overcrowding_issue/ |


---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size: 150**

**Overlap: 25**

**Reasoning:This size is large enough to contain information from the student review and also big enough that a specific section from the official webpages will be able to fit in one chunk without it containing multiple different topics (if the chunk size was larger). If we used smaller chunks then we risk having fragmented information and incomplete student reviews from some of the sources. The overlap ensures that any information that is around the chunk borders is still able to be retrieved and used.**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model: all-MiniLM-L6-V2 via sentence transformers**

**Top-k: 5**

**Production tradeoff reflection: Accuracy vs speed - Larger embedding models generally produce higher-quality embeddings and retrieve more relevant documents, especially when users phrase questions differently from the source text. However, larger models also have higher latency and require more computational resources.Local vs api hosted - Local models like the one I am using for this project are free and have all the data on the machine but is typically less accurate than hosted models. Api- hosted models Context length limits - Embedding models have different limits on how long the chunking size can be. For this project most of the sources are small enough that the limit is not a concern.**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Which dorm is the best choice for a freshman who wants a social environment and easy access to campus resources?| Watterson towers is a good choice for freshman seeking a social environment as students have described it as having a large population which makes it easy to meet people. It is also a central location and has study spaces.|
| 2 | What are the biggest complaints students have about living in Watterson Towers, and do the benefits outweigh the drawbacks?| Students have identified that there are long elevator wait times during busy periods, the building is pretty big which makes it confusing to navigate, high noise levels due to high population. In spite of these concerns, there are strong social opportunities and convenient areas to study, eat and hang out. Overall, students have noted that watterson has some issues due to its large size but the social opportunities and convenience outweights that issue.|
| 3 |How does the roommate selection process work, and what advice do current students give for finding a good roommate? | The roomate selection process happens through the university housing application system. In that portal students are able to look for roomates based on interests, housing preferences and themed living-learnign communities. Current students recommend: discussing sleep and study schedules early, talk about expectations like clenliness, reaching out to a variety of people, being honest about preferences to avoid later conflict. |
| 4 |What housing rules and policies should new residents be aware of before moving into an ISU residence hall? | New students should be aware of: guest and visitation policies, prohibited items within residence halls, safety and fire regulations and housing contract obligations.
Room condition and damage responsibilities, check-in and move-out procedures.|
| 5 | Is overcrowding a significant issue in ISU housing, and how has it affected students' living experiences?| Student discussions indicate that overcrowding has been a concern during some housing cycles. Reported effects include: increased demand for housing spaces, greater competition for preferred room assignments, more crowded common areas and facilities. 
However, official housing information shows that the university has housing assignments to manage this. Some students have reported a minimal disruption while others state that there are some noticeable impacts on housing comfort.|

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. With many subjective responses on the reddir sources, the large amount of contrasting opinions on the forms could confuse the model and result with imporoper generation. At least, it may not answer the question to the extent that is helpful.

2. As there are only 13 sources, there will be incomplete information so the generation would not answer the questions to the best possible level.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->
ISU Housing Documents
        |
        v
+-----------------------+
| Chunking              |
| 500 tokens            |
| 100 overlap           |
+-----------------------+
        |
        v
+-----------------------+
| all-MiniLM-L6-v2      |
| Embedding Model       |
+-----------------------+
        |
        v
+-----------------------+
| ChromaDB              |
| Vector Store          |
+-----------------------+
        ^
        |
   User Query
        |
        v
+-----------------------+
| Similarity Retrieval  |
| Top-k = 5             |
+-----------------------+
        |
        v
+-----------------------+
|llama-3.3-70b-versatile|
| Answer Generation     |
+-----------------------+
        |
        v
   Cited Response

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking: I asked Claude to to look over my source files to ensure they were all formatted in the same way. I was expecting it to confirm and maybe give some alternative suggestions. I also asked it to look over my chunking strategy and to use it develop the methods in ingest.py to get chunks from the sources. I looked over and ensured there were no issues with the response**

**Milestone 4 — Embedding and retrieval: I told claude to help implement the embedding and retrieval methods in vector_store.py using all-MiniLM-L6-V2. I told it about my prefrences, top-k and expected tradeoffs. After checking the response, I looked to see if it followed my directions and if there was anything to change**

**Milestone 5 — Generation and interface: I sent the flowchart diagram for the rag pipeline and my grounding statements and asked it to generate code to enable the llm to generate statements from the chunks. I edited the chunk size and overlap to fit my needs and also needed to replace deprecated settings and disable windows firewall for the folder as it was blocking sklearn ddl.**
