# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

The domain I chose was university dorming. Although there are websites that have information about them, there is no single one spot that easily lets you see the differences and decide which is better so I chose this as the domain to make it easier for incoming students. This information is valuable as it allows incoming students to know which housing would be the best for them.

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size: 150**

**Overlap: 25**

**Why these choices fit your documents: This size is large enough to contain information from the student review and also big enough that a specific section from the official webpages will be able to fit in one chunk without it containing multiple different topics (if the chunk size was larger). If we used smaller chunks then we risk having fragmented information and incomplete student reviews from some of the sources. The overlap ensures that any information that is around the chunk borders is still able to be retrieved and used.**

**Final chunk count: 55**

**5 Example chunks:

{
    "id": "hewett_manchester_official_guide.txt-1",
    "source": "hewett_manchester_official_guide.txt",
    "chunk_index": 1,
    "chunk_size": 150,
    "text": "Source: Hewett-Manchester Official Guide URL: https://housing.illinoisstate.edu/locations/hewett-manchester/ SECTION: Overview The Hewett-Manchester residential area consists of two 18-story residence halls located a short distance from Milner Library and the Bone Student Center. The community includes: - Themed Living-Learning Communities (TLLCs) - An outdoor basketball court - The Visor Tutoring Center All room furniture is movable, and beds can be lofted or bunked at different heights. Hewett-Manchester offers nine-month housing, meaning it remains open during university breaks. --- SECTION: Location and Campus Access Hewett-Manchester is located within walking distance of major campus resources, including: - Milner Library - Bone Student Center - Academic buildings on central campus --- SECTION: Dining Options Students in Hewett-Manchester typically dine at the Watterson Dining Commons, which is located a short walk away. Additional options include: - Subway in Manchester Hall - Various on-campus and nearby dining locations --- SECTION: Study Spaces Hewett-Manchester provides multiple study and academic"
  },

  {
    "id": "hewett_manchester_official_guide.txt-2",
    "source": "hewett_manchester_official_guide.txt",
    "chunk_index": 2,
    "chunk_size": 150,
    "text": "Additional options include: - Subway in Manchester Hall - Various on-campus and nearby dining locations --- SECTION: Study Spaces Hewett-Manchester provides multiple study and academic support spaces, including: - Kong Room (reservable study space) - Vrooman/Visor Center Lounge (near tutoring center) - Visor Tutoring Center --- SECTION: Recreational and Community Spaces Available facilities include: - Piano and music practice rooms (located in the Vrooman Center) - Outdoor basketball court - Community lounges --- SECTION: Laundry Facilities Laundry rooms are located in the basement of each building and are accessible 24/7. Laundry use is included in housing costs. Students may use both high-efficiency (HE) and standard detergent. Machine availability and timing can be tracked using LaundryView at laundryview.com. --- SECTION: Room Layout Options Hewett Hall and Manchester Hall offer the following room types: Hewett Hall: - Single rooms - Double rooms - Double suite options - Quad rooms Manchester Hall: -"
  },

  {
    "id": "hewett_manchester_official_guide.txt-3",
    "source": "hewett_manchester_official_guide.txt",
    "chunk_index": 3,
    "chunk_size": 150,
    "text": "Manchester Hall offer the following room types: Hewett Hall: - Single rooms - Double rooms - Double suite options - Quad rooms Manchester Hall: - Single rooms - Double rooms - Double suite options - Quad rooms Furniture is moveable, and beds can be lofted or bunked. --- SECTION: Floor Designations and Living Communities Hewett-Manchester offers themed and identity-based floors, including: - Academic and Career Exploration - Business - Health & Wellness - Information Technology - Mathematics - Nursing - Social Work - Special Education - Honors - Leadership - Music - Fine Arts - Global Perspectives - Rainbow Floor - Teacher Education These communities are designed to support academic, social, and personal development. Bathroom options include gender-neutral, male, and female facilities in select floors across Hewett and Manchester. --- SECTION: Themed Living-Learning Communities (TLLCs) Hewett-Manchester hosts multiple TLLCs that connect students with shared academic or personal interests. These communities"
  },

  {
    "id": "hewett_manchester_official_guide.txt-4",
    "source": "hewett_manchester_official_guide.txt",
    "chunk_index": 4,
    "chunk_size": 150,
    "text": "across Hewett and Manchester. --- SECTION: Themed Living-Learning Communities (TLLCs) Hewett-Manchester hosts multiple TLLCs that connect students with shared academic or personal interests. These communities aim to enhance learning and build social connections within the residence halls. --- SECTION: Refrigerator Policy Students are allowed to bring refrigerators into their rooms, provided they do not exceed: - 4.5 cubic feet in size - 1.5 running amps University Housing Services does not provide or rent refrigerators. --- SECTION: What Students Should Bring Recommended items include: - Bedding (extra-long twin) - Computer and headphones - Desk lamp (non-halogen) - Alarm clock - Shower shoes and towels - Bathrobe and bathroom caddy - First aid kit - Garbage can - Umbrella - Iron --- SECTION: Housing Summary Hewett-Manchester provides a residential experience that combines academic support, themed communities, and access to campus resources. Its nine-month housing availability makes it suitable for students who wish"
  },

  {
    "id": "hewett_manchester_official_guide.txt-5",
    "source": "hewett_manchester_official_guide.txt",
    "chunk_index": 5,
    "chunk_size": 31,
    "text": "a residential experience that combines academic support, themed communities, and access to campus resources. Its nine-month housing availability makes it suitable for students who wish to remain on campus during breaks."
  },

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used: For this project, I will use the recommended model which is all-MiniLM-L6-v2. It is run locally and is tokenless making it a great choice for this project. If I were making this a real project and cost were not a constraint then I would use open ai's text-embedding-3-large model as it have very strong semantic retrieval performance and can understand paraphrased questions better. This higher quality model will also have better retrieval accuracy in general.**

**Production tradeoff reflection: Accuracy vs speed - Larger embedding models generally produce higher-quality embeddings and retrieve more relevant documents, especially when users phrase questions differently from the source text. However, larger models also have higher latency and require more computational resources.Local vs api hosted - Local models like the one I am using for this project are free and have all the data on the machine but is typically less accurate than hosted models. Api- hosted models Context length limits - Embedding models have different limits on how long the chunking size can be. For this project most of the sources are small enough that the limit is not a concern.**

**Example retrieval test examples
Question 1: Which dorm is the best choice for a freshman who wants a social environment and easy access to campus resources?
first chunk: 

reddit_housing_discussion.txt, chunk 3, distance 0.363479
Chunk text begins with:
“Bigger room sizes and easier to make friends.” --- Tri-Towers - Generally considered farther from most academic buildings and campus core - Strong benefit: on-site dining hall and bus access..."
second chunk: 

reddit_best_dorm.txt, chunk 1, distance 0.381816
Chunk text begins with:
Source: Reddit “Best Dorm?” (Illinois State University Housing Discussion) ... Watterson Towers - Very popular and social - Closest dorm to the Quad ...
Third chunk:

reddit_pros_and_cons_isu_dorms.txt, chunk 1, distance 0.397578
Chunk text begins with:
Source: Reddit “Pros & Cons of ISU Dorms (A Freshman’s Guide)” ... SECTION: Watterson Towers — Advantages ... Proximity and Convenience ... Dining Access ...


Question 2: What are the biggest complaints students have about living in Watterson Towers, and do the benefits outweigh the drawbacks?

First chunk:
reddit_honest_dorm_review.txt, chunk 1, distance 0.259945
Chunk text begins with:
Source: Reddit “Honest Dorm Review (Watterson Towers)” ... SECTION: Overall Summary ... Watterson Towers as having both strong benefits and significant drawbacks ...

Second chunk:
reddit_housing_discussion.txt, chunk 2, distance 0.277447
Chunk text begins with:
and is easy to navigate.” --- Watterson Towers (Watty) - Very large, busy, and high-traffic residence hall - Known for long elevator wait times and crowding ...

third chunk:
reddit_pros_and_cons_isu_dorms.txt, chunk 5, distance 0.297134
Chunk text begins with:
main academic buildings. Disadvantage: Social and Environmental Noise ... Disadvantage: Off-Campus Distance ... Comment: Room Size Comparison ...

For this question, the first chunk contains informatino about some benefits and drawbacks of watterson, the second chunk talks about the business of it, and the third chunk has information on the loud noises and distances from other spots on campus. All three of these chunks relate to the query.

Question 3: How does the roommate selection process work, and what advice do current students give for finding a good roommate?
First chunk:
reddit_roomate.txt, chunk 1, distance 0.401498
Chunk text begins with:
Roommate Selection with TLLCs SECTION: Author Context ... Reddit users explain that while there isn’t a direct filter for honors floor approval, messaging multiple matches and using social media groups are effective strategies.
Second chunk:
reddit_roomate.txt, chunk 2, distance 0.459250
Chunk text begins with:
deposits. Tip: Message Multiple Matches ... Tip: Use Social Media ... Patience is Key ...
Third chunk:
international_student_housing.txt, chunk 3, distance 0.529988
Chunk text begins with:
required PRIVATELY OWNED APARTMENTS (OFF-CAMPUS HOUSING) - Managed by private landlords, not the university ... Roommate finder tool ...


For this question the first chunk talks about the filtering process for roomate, the second talks about using social media to find suitable roomates, and the third chunk talks about the roomate finder tool on the official website. All 3 of these are related to the query about the roomate selection process.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:Answer the question using only the information in the provided documents.If the documents don't contain enough information to answer, say 'I don't have enough information on that. Ensure the answers are from received text only and with source attribution. Return the result using the exact format: (Answer) + (SourceList)**

**The grounding instruction clearly defines how the llm should respond if there is not enough information to answer a query**

**How source attribution is surfaced in the response: In the grounding instruction the last line talks about the general format for the response. In the method it is used, it is written in a proper way. Here it was changed to be more readable, but the idea is the same: clearly defining how the model should generate responses. This ensures that that the sources that were used are listed.**

**Example of out of scope query with system refusal 
query "How does UIUC ISR compare to ISU's watterson dining hall?"
Answer: I don't have enough information on that.
Sources: reddit_pros_and_cons_isu_dorms.txt, reddit_housing_discussion.txt, reddit_best_dorm.txt 

(Note: The provided documents do not mention UIUC ISR, so it's impossible to compare it to ISU's Watterson dining hall based on the given information.)**

**Two system responses with source attribution:

 "What housing rules and policies should new residents be aware of before moving into an ISU residence hall?"
Answer: New residents should be aware of the following housing rules and policies: Accountability Standards, Housing Behavior Policies, Access policies (residence halls are secured 24/7 and require a Redbird ID for entry), Keys and Identification policies (residents must carry their ID and room key at all times), Room Change Policy, Room Condition & Cleanliness policies, Smoke and Tobacco Policy, Sports in Halls policy, Sprinkler Systems policy, Student Room Policies (including furniture, decorations, open flame, and trash policies), Safety Policies (including Fire Safety, Emergency Equipment, and Harassment policies), and Room Entry and Search policies.
Sources: residence_hall_policies.txt

Second example:
query "Is overcrowding a significant issue in ISU housing, and how has it affected students' living experiences?"
Answer: Overcrowding is a significant issue in ISU housing, particularly in freshman housing, with students being placed in lounge spaces or overcrowded dorm setups, although opinions differ on the severity and causes. It has affected students' living experiences, with varying impacts depending on year, housing assignment, and timing of enrollment.
Sources: reddit_overcrowding.txt, reddit_housing_discussion.txt, reddit_pros_and_cons_isu_dorms.txt**

** The query interface has a dialog box to enter in the query, a slider to change topk value (used for debugging purposes), and a button to submit the question. The output has its own dialog box with space for the llm generation.
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 |Which dorm is the best choice for a freshman who wants a social environment and easy access to campus resources? | Watterson towers is a good choice for freshman seeking a social environment as students have described it as having a large population which makes it easy to meet people. It is also a central location and has study spaces. | Watterson towers is best for social life and room size, but can be crowded. |Relevant | partially accurate |
| 2 | What are the biggest complaints students have about living in Watterson Towers, and do the benefits outweigh the drawbacks?| Students have identified that there are long elevator wait times during busy periods, the building is pretty big which makes it confusing to navigate, high noise levels due to high population. In spite of these concerns, there are strong social opportunities and convenient areas to study, eat and hang out. Overall, students have noted that watterson has some issues due to its large size but the social opportunities and convenience outweights that issue.| Biggest issues include elevator delays and wait times, frequent fire alarms, high population density, crowding, and concerns about cleanliness. While Watterson Towers has benefits such as a strong social environment, easy access to campus, larger room sizes, and natural light and views, the drawbacks may outweigh these advantages for some students | relevant | accurate |
| 3 | How does the roommate selection process work, and what advice do current students give for finding a good roommate?| The roomate selection process happens through the university housing application system. In that portal students are able to look for roomates based on interests, housing preferences and themed living-learnign communities. Current students recommend: discussing sleep and study schedules early, talk about expectations like clenliness, reaching out to a variety of people, being honest about preferences to avoid later conflict.|  The roommate selection process involves checking the TLLC approval individually on potential roommates' profiles, messaging multiple matches to increase the chances of finding a compatible roommate, and using social media groups to connect with other students. Students advised to be patient. | relevant | accurate |
| 4 | What housing rules and policies should new residents be aware of before moving into an ISU residence hall?| New students should be aware of: guest and visitation policies, prohibited items within residence halls, safety and fire regulations and housing contract obligations. Room condition and damage responsibilities, check-in and move-out procedures.| Accountability Standards, Housing Behavior Policies, Access policies (24/7 secured residence halls, Redbird ID required for entry), Keys and Identification policies (residents must carry ID and room key(s) at all times), Room Change Policy, Room Condition & Cleanliness, Smoke and Tobacco Policy, Sports in Halls, Sprinkler Systems, Student Room Policies (furniture, decorations, open flame, trash), Safety Policies (Fire Safety, Emergency Equipment, Harassment), and Room Entry and Search policies. | relevant | accurate |
| 5 | Is overcrowding a significant issue in ISU housing, and how has it affected students' living experiences?|Student discussions indicate that overcrowding has been a concern during some housing cycles. Reported effects include: increased demand for housing spaces, greater competition for preferred room assignments, more crowded common areas and facilities. However, official housing information shows that the university has housing assignments to manage this. Some students have reported a minimal disruption while others state that there are some noticeable impacts on housing comfort.| Overcrowding is a huge issue, with some students placed into crowded dorms. The issue is caused by incresing enrollment with minimal personal impact.| Relevant | Partially accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed: "Is cardinal courts a good dorm for sophomores at ISU who plan on living solo?"**

**What the system returned: Cardinal Court is a suitable option for sophomores, as it houses approximately 994 undergraduate students, primarily sophomores, and offers apartment-style living with furnished apartments and an independent living environment.**

**Root cause (tied to a specific pipeline stage): This seems to be an issue in the retrieval phase as there was information for single bed apartments, yet it failed to identify and use that in the generation.**

**What you would change to fix it: I would try to improve the accuracy by adding clearer/better metadata tags so the model can filter through the information better**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation: The definitions for the chunking strategy allowed the ai agent to develop the methods pretty accurately and did not require that much alterations from me for it to work properly.**

**One way your implementation diverged from the spec, and why: I ended up changing the chunking character size and the overflow amount to fit my source texts a little better.**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI: Is this question good for a rag pipeline? Which dorm is best for freshmen?*
- *What it produced: As it stands, no, this is a bad question for a Retrieval-Augmented Generation (RAG) pipeline. However, it is a bad question because of the context, not the technology. If you tweak how you handle it, it can become a perfect RAG use case. 1. It lacks a specific scope (The "Which University?" Problem) 2. It is highly subjective Step 1: Force scope in the prompt or metadata
You must inject the specific institution.

Bad: "Which dorm is best for freshmen?"

Good: "Which dorm is best for freshmen at The University of Michigan?"*
- *What I changed or overrode: I took the advice and then applied it to my own pipeline by making my questions more specific and not stuff that could be found through official means*

**Instance 2**

- *What I gave the AI: how to unblock sklearn ddl (was having an error)*
- *What it produced:Update/Reinstall the DependenciesOften, a DLL load error is caused by version mismatches in Scikit-Learn's underlying libraries like NumPy or SciPy.Run the following commands in your terminal or command prompt:bashpip uninstall -y scikit-learn numpy scipy
pip install --upgrade scikit-learn numpy scipy*
- *What I changed or overrode: I decided to refresh my venv and then check windows security settings and disabled overview for the folder*
