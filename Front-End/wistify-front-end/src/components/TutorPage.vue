<template>
  <NavBar />
  <div v-if="currentTutor" :key="currentTutor.id">
    <div class="banner">
      <img src="/Background_Blur.svg" alt="Tutor Banner" />
    </div>

    <div class="tutor-info">
      <h2 class="tutor-name">{{ currentTutor.name }}</h2>
      <p class="tutor-subjects">{{ currentTutor.subjects.join(", ") }}</p>
      <br>
      <p class="tutor-rating">Rating: {{ currentTutor.rating }}/5</p>
      <p class="description">{{ currentTutor.description }}</p>

      <div class="contact-section">
        <div class="contact-info">
          <div>Email: {{ currentTutor.email }}</div>
          <div>Tel: {{ currentTutor.tel }}</div>
        </div>
        <button @click="contactTutor(currentTutor)" class="contact-button">Contact Tutor</button>
      </div>
    </div>

    <div class="content-section">
      <h3 class="section-title">Learning Resources</h3>
      <div v-for="resource in currentTutor.resources" :key="resource.id" class="resource">
        <iframe :src="resource.videoLink" frameborder="0" allowfullscreen></iframe>
        <p class="resource-description">{{ resource.description }}</p>
      </div>
    </div>

    <hr /> <!-- Add a horizontal line between tutors for separation -->

    <!-- Comment and Rating Section -->
    <div class="comment-rating-section">
      <h3 class="section-title">Comments and Ratings</h3>
      <div v-for="comment in currentTutor.comments" :key="comment.id" class="comment">
        <div class="comment-info">
          <div class="comment-author">{{ comment.author }}</div>
          <div class="comment-date">{{ comment.date }}</div>
        </div>
        <p class="comment-text">{{ comment.text }}</p>
        <div class="comment-rating">Rating: {{ comment.rating }}/5</div>
      </div>
    </div>

    <hr /> <!-- Add a horizontal line between comments and tutors for separation -->

    <div class="navigation-buttons">
      <button @click="prevTutor" :disabled="currentIndex === 0">Previous Tutor</button>
      <button @click="nextTutor" :disabled="currentIndex === tutors.length - 1">Next Tutor</button>
    </div>
  </div>
  <div v-else>
    Tutor not found.
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";

export default {
  components: { NavBar },
  data() {
    return {
      tutors:  [
        {
          id: 2,
          name: "Jill Smith",
          subjects: ["Physics", "Mechanics"],
          rating: 3.8,
          bannerImg: "/public/item2.jpg",
          email: "jill.smith@example.com",
          tel: "987-654-3210",
          description: "Explore the fascinating world of physics with an experienced tutor.",
          resources: [
            {
              id: 1,
              videoLink: "https://www.youtube.com/embed/your-video-id-1",
              description: "Resource 1 description",
            },
            {
              id: 2,
              videoLink: "https://www.youtube.com/embed/your-video-id-2",
              description: "Resource 2 description",
            },
          ],
          comments: [
            {
              id: 1,
              author: "John Doe",
              date: "2023-01-01",
              text: "Jill is an amazing tutor! I learned a lot from her.",
              rating: 5,
            },
            {
              id: 2,
              author: "Jane Smith",
              date: "2023-02-15",
              text: "Jill explains complex concepts in a simple way. Highly recommended!",
              rating: 4,
            },
          ],
        },
        {
          id: 3,
          name: "Sarah Johnson",
          subjects: ["Chemistry", "Organic Chemistry"],
          rating: 4.2,
          bannerImg: "/public/item3.jpg",
          email: "sarah.johnson@example.com",
          tel: "123-456-7890",
          description: "Dive into the principles of chemistry and organic chemistry with Sarah.",
          resources: [
            {
              id: 3,
              videoLink: "https://www.youtube.com/embed/your-video-id-3",
              description: "Resource 3 description",
            },
            {
              id: 4,
              videoLink: "https://www.youtube.com/embed/your-video-id-4",
              description: "Resource 4 description",
            },
          ],
        },
        {
          id: 4,
          name: "Alex Miller",
          subjects: ["Computer Science", "Programming"],
          rating: 4.0,
          bannerImg: "/public/item4.jpg",
          email: "alex.miller@example.com",
          tel: "555-123-4567",
          description: "Learn coding and programming concepts from an expert in computer science.",
          resources: [
            {
              id: 5,
              videoLink: "https://www.youtube.com/embed/your-video-id-5",
              description: "Resource 5 description",
            },
            {
              id: 6,
              videoLink: "https://www.youtube.com/embed/your-video-id-6",
              description: "Resource 6 description",
            },
          ],
        },
        {
          id: 5,
          name: "Emily Davis",
          subjects: ["English Literature", "Writing"],
          rating: 4.7,
          bannerImg: "/public/item5.jpg",
          email: "emily.davis@example.com",
          tel: "987-654-3210",
          description: "Enhance your literary skills with Emily's comprehensive English literature and writing sessions.",
          resources: [
            {
              id: 7,
              videoLink: "https://www.youtube.com/embed/your-video-id-7",
              description: "Resource 7 description",
            },
            {
              id: 8,
              videoLink: "https://www.youtube.com/embed/your-video-id-8",
              description: "Resource 8 description",
            },
          ],
        },
      ],
      currentTutor: null,
      currentIndex: 0,
    };
  },
  watch: {
    $route: "fetchTutor",
  },
  mounted() {
    this.fetchTutor();
  },
  methods: {
    fetchTutor() {
      const tutorId = parseInt(this.$route.params.id);
      console.log("Fetching tutor...");
      if (!isNaN(tutorId)) {
        console.log("Tutor ID:", tutorId);
        const tutor = this.tutors.find((t) => t.id === tutorId);

        if (tutor) {
          console.log("Tutor found:", tutor);
          this.currentTutor = tutor;
          this.currentIndex = this.tutors.indexOf(tutor);
        } else {
          console.log("Tutor not found");
          this.currentTutor = null;
          this.currentIndex = 0;
        }
      } else {
        console.log("Invalid tutor ID");
        this.currentTutor = null;
        this.currentIndex = 0;
      }
    },
    contactTutor(tutor) {
      console.log("Contacting tutor:", tutor.name);
      // Implement logic to contact the tutor
    },
    prevTutor() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
        this.currentTutor = this.tutors[this.currentIndex];
      }
    },
    nextTutor() {
      if (this.currentIndex < this.tutors.length - 1) {
        this.currentIndex++;
        this.currentTutor = this.tutors[this.currentIndex];
      }
    },
  },
};
</script>

<style scoped>
/* Add your scoped styles here */
.banner {
  height: 600px;
  overflow: hidden;
}

.banner img {
  width: 100%;
  height: auto;
}

.tutor-info {
  padding: 20px;
}

.tutor-name {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.description {
  color: #555;
  margin-bottom: 20px;
}

.contact-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.contact-info {
  flex: 1;
}

.contact-button {
  background-color: #B8E830;
  color: #000000;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.content-section {
  margin-top: 20px;
}

.section-title {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.resource {
  margin-bottom: 10px;
}

iframe {
  width: 100%;
  max-width: 600px;
  height: 250px;
}

.resource-description {
  color: #777;
}

.comment-rating-section {
  margin-top: 20px;
}

.comment {
  margin-bottom: 20px;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}

.comment-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.comment-text {
  margin-bottom: 10px;
}

.comment-rating {
  color: #B8E830;
}
</style>
