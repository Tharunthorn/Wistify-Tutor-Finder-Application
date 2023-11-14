<template>
  <div>
    <NavBar />
    <div class="main-container">
      <div class="search-container">
        <input
            v-model="searchTerm"
            @input="searchItems"
            type="text"
            placeholder="Search..."
            class="search-bar"
        />
      </div>

      <div v-if="filteredItems.length > 0" class="item-grid">
        <router-link
            v-for="item in filteredItems"
            :key="item.id"
            :to="'/Tutor/' + item.id"
            class="item-card"
        >
          <!-- Display item information here -->
          <div class="item-image" :style="{ backgroundImage: 'url(' + item.banner + ')' }"></div>
          <div class="item-details">
            <div class="item-name font-semibold">{{ item.name }}</div>
            <div class="item-subjects text-gray-500">
              <span v-for="(subject, index) in item.subjects" :key="index">
                {{ subject }}
                <span v-if="index < item.subjects.length - 1">, </span>
              </span>
            </div>
            <div class="item-rating">Rating: {{ item.rating }}</div>
            <div class="item-description">{{ item.description }}</div>
          </div>
          <!-- Add more item details as needed -->
        </router-link>
      </div>

      <div v-if="filteredItems.length === 0" class="no-items-found">
        No items found.
      </div>
    </div>

    <div class="footer">
      <p class="footer-text">© 2023 Wistify. All rights reserved.</p>
    </div>
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";

export default {
  components: { NavBar },
  data() {
    return {
      searchTerm: this.$route.query.searchTerm || "", // Use $route.query instead of $route.params
      items: [
        {
          id: 1,
          name: "Mark Robinson",
          subjects: ["Math", "Algebra", "Geometry"],
          rating: 4.5,
          banner: "item1.jpg",
          description: "This is a math tutoring session covering various topics.",
        },
        {
          id: 2,
          name: "Jill Smith",
          subjects: ["Physics", "Mechanics"],
          rating: 3.8,
          banner: "item2.jpg",
          description: "Explore the fascinating world of physics with an experienced tutor.",
        },
        {
          id: 3,
          name: "Sarah Johnson",
          subjects: ["Chemistry", "Organic Chemistry"],
          rating: 4.2,
          banner: "item3.jpg",
          description: "Dive into the principles of chemistry and organic chemistry with Sarah.",
        },
        {
          id: 4,
          name: "Alex Miller",
          subjects: ["Computer Science", "Programming"],
          rating: 4.0,
          banner: "item4.jpg",
          description: "Learn coding and programming concepts from an expert in computer science.",
        },
        {
          id: 5,
          name: "Emily Davis",
          subjects: ["English Literature", "Writing"],
          rating: 4.7,
          banner: "item5.jpg",
          description: "Enhance your literary skills with Emily's comprehensive English literature and writing sessions.",
        },
        {
          id: 6,
          name: "Ryan Turner",
          subjects: ["History", "World History"],
          rating: 3.9,
          banner: "item6.jpg",
          description: "Explore the richness of history and world events with Ryan's engaging tutoring sessions.",
        },
        {
          id: 7,
          name: "Sophie Anderson",
          subjects: ["Biology", "Genetics"],
          rating: 4.4,
          banner: "item7.jpg",
          description: "Delve into the mysteries of biology and genetics with Sophie's expert guidance.",
        },
        {
          id: 8,
          name: "David Chen",
          subjects: ["Economics", "Microeconomics"],
          rating: 4.1,
          banner: "item8.jpg",
          description: "Understand economic principles and microeconomics with David's informative sessions.",
        },
        {
          id: 9,
          name: "Laura Rodriguez",
          subjects: ["Spanish", "Language Arts"],
          rating: 4.3,
          banner: "item9.jpg",
          description: "Improve your Spanish language skills and excel in language arts with Laura's personalized tutoring.",
        },
        {
          id: 10,
          name: "Chris Taylor",
          subjects: ["Chemical Engineering", "Thermodynamics"],
          rating: 4.6,
          banner: "item10.jpg",
          description: "Gain a deep understanding of chemical engineering and thermodynamics with Chris's expert guidance.",
        },
        {
          id: 11,
          name: "Mia Campbell",
          subjects: ["Psychology", "Counseling"],
          rating: 4.2,
          banner: "item11.jpg",
          description: "Explore the world of psychology and counseling with Mia's insightful sessions.",
        },
        {
          id: 12,
          name: "Dylan White",
          subjects: ["Art History", "Painting"],
          rating: 4.8,
          banner: "item12.jpg",
          description: "Appreciate art history and refine your painting skills with Dylan's creative tutoring.",
        },
        {
          id: 13,
          name: "Isabella Kim",
          subjects: ["Statistics", "Probability"],
          rating: 4.5,
          banner: "item13.jpg",
          description: "Master statistical concepts and probability with Isabella's tailored tutoring approach.",
        },
        {
          id: 14,
          name: "Jordan Patel",
          subjects: ["Political Science", "International Relations"],
          rating: 4.0,
          banner: "item14.jpg",
          description: "Explore political science and international relations with Jordan's informative sessions.",
        },
        {
          id: 15,
          name: "Eva Nguyen",
          subjects: ["Environmental Science", "Sustainability"],
          rating: 4.3,
          banner: "item15.jpg",
          description: "Understand environmental science and sustainability with Eva's engaging tutoring.",
        },
        {
          id: 16,
          name: "Nathan Harris",
          subjects: ["Geography", "Cartography"],
          rating: 4.5,
          banner: "item16.jpg",
          description: "Explore the world through geography and cartography with Nathan's interactive sessions.",
        },
        {
          id: 17,
          name: "Olivia Turner",
          subjects: ["French", "Language Arts"],
          rating: 4.2,
          banner: "item17.jpg",
          description: "Immerse yourself in the beauty of the French language and language arts with Olivia's guidance.",
        },
        {
          id: 18,
          name: "Jason Lewis",
          subjects: ["Sociology", "Social Sciences"],
          rating: 4.4,
          banner: "item18.jpg",
          description: "Understand societal dynamics and social sciences with Jason's thought-provoking sessions.",
        },
        {
          id: 19,
          name: "Lily Chen",
          subjects: ["Anthropology", "Cultural Studies"],
          rating: 4.1,
          banner: "item19.jpg",
          description: "Explore human cultures and cultural studies with Lily's insightful tutoring.",
        },
        {
          id: 20,
          name: "Caleb Rodriguez",
          subjects: ["Music Theory", "Piano"],
          rating: 4.6,
          banner: "item20.jpg",
          description: "Deepen your understanding of music theory and piano with Caleb's musical expertise.",
        },
        {
          id: 21,
          name: "Zoe Brown",
          subjects: ["Astrophysics", "Astronomy"],
          rating: 4.7,
          banner: "item21.jpg",
          description: "Embark on a cosmic journey with Zoe to explore astrophysics and astronomy.",
        },
        {
          id: 22,
          name: "Elijah Martinez",
          subjects: ["Political Philosophy", "Ethics"],
          rating: 4.3,
          banner: "item22.jpg",
          description: "Delve into political philosophy and ethics with Elijah's thought-provoking discussions.",
        },
        {
          id: 23,
          name: "Ava Thompson",
          subjects: ["Drama", "Acting"],
          rating: 4.8,
          banner: "item23.jpg",
          description: "Unleash your creativity through drama and acting with Ava's dynamic tutoring sessions.",
        },
        {
          id: 24,
          name: "Noah Garcia",
          subjects: ["Physical Education", "Fitness"],
          rating: 4.0,
          banner: "item24.jpg",
          description: "Stay fit and healthy with Noah's guidance in physical education and fitness.",
        },
        {
          id: 25,
          name: "Maya Patel",
          subjects: ["Digital Marketing", "Social Media"],
          rating: 4.5,
          banner: "item25.jpg",
          description: "Navigate the world of digital marketing and social media with Maya's expert insights.",
        },
        {
          id: 26,
          name: "Gabriel Taylor",
          subjects: ["Computer Science", "Data Structures"],
          rating: 4.2,
          banner: "item26.jpg",
          description: "Master data structures and algorithms with Gabriel's comprehensive computer science tutoring.",
        },
        {
          id: 27,
          name: "Sophia Lee",
          subjects: ["Math", "Calculus"],
          rating: 4.6,
          banner: "item27.jpg",
          description: "Dive into advanced calculus concepts with Sophia's expert guidance in mathematics.",
        },
        {
          id: 28,
          name: "Daniel Brown",
          subjects: ["Physics", "Optics"],
          rating: 4.4,
          banner: "item28.jpg",
          description: "Explore the fascinating world of optics and light physics with Daniel's insightful sessions.",
        },
        {
          id: 29,
          name: "Aiden Miller",
          subjects: ["Chemistry", "Inorganic Chemistry"],
          rating: 4.1,
          banner: "item29.jpg",
          description: "Understand the principles of inorganic chemistry with Aiden's informative tutoring sessions.",
        },
        {
          id: 30,
          name: "Olivia Davis",
          subjects: ["English Literature", "Poetry"],
          rating: 4.7,
          banner: "item30.jpg",
          description: "Appreciate the art of poetry and literature with Olivia's engaging English literature sessions.",
        },
        // Add more items as needed
      ],
    };
  },
  watch: {
    '$route.query.searchTerm': function (newSearchTerm) {
      this.searchTerm = newSearchTerm || "";
      this.searchItems(); // trigger search on route change
    },
  },
  created() {
    // Fetch data or perform any other initialization here
    // You can also trigger the search here if needed
  },
  computed: {
    filteredItems() {
      if (!this.searchTerm) return this.items;

      const searchTerm = this.searchTerm.toLowerCase();
      return this.items.filter(
          (item) =>
              item.name.toLowerCase().includes(searchTerm) ||
              item.subjects.some((subject) => subject.toLowerCase().includes(searchTerm))
      );
    },
  },
  methods: {
    searchItems() {
      // Perform real-time search
    },
  },
};
</script>

<style>
/* Reset some default styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Apply a global font and set a default background color */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f4f4;
}

/* Style the main container */
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ffffff;
  min-height: 100vh;
  margin-top: 100px;
}

/* Style the search container */
.search-container {
  width: 70%;
  max-width: 2xl;
  padding: 4;
  margin-bottom: 40px; /* Added margin-bottom */
}

/* Style the item grid */
.item-grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1rem;

  @media (min-width: 640px) {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  @media (min-width: 1280px) {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

/* Style the item cards */
/* Style the item cards with smooth hover effect */
.item-card {
  width: 300px;
  height: 400px; /* Increased height to accommodate the description */
  background-color: #f3f4f6;
  padding: 1rem;
  border-radius: 0.375rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.10);
  transition: transform 0.3s ease-in-out; /* Add a smooth transition effect */

  &:hover {
    transform: scale(1.05); /* Increase the size on hover */
  }
}

/* Style the item image */
.item-image {
  background-size: cover;
  background-position: center;
  height: 150px;
  border-radius: 0.375rem;
  /* Set background color when there is no image or it fails to load */
  background-color: #ccc; /* Choose a color of your preference */
}

/* Style the item details */
.item-details {
  flex-grow: 1;
}

.item-name {
  color: #8CB024;
  font-weight: 600;
}

.item-subjects {
  color: #6b7280;
}

.item-rating {
  margin-top: 10px;
  font-weight: 500;
  color: #000;
}

.item-description {
  margin-top: 10px;
  color: #333; /* Set the color for the description */
  font-size: 0.9rem;
}

/* Style the no items found message */
.no-items-found {
  text-align: center;
  color: #6b7280;
}

/* Style the search bar */
.search-bar {
  font-family: 'Montserrat', sans-serif;
  width: 100%;
  height: 2.5rem;
  background-color: #FFF;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.10);
  border-radius: 0.469rem;
  padding: 0.5rem 1rem;
  border: none;
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.4);
}

/* Footer styles */
.footer {
  margin-bottom: 2rem;
  width: 100%;
  height: 30px;
}

.footer-text {
  margin-top: 4rem;
  color: #000000; /* Text color */
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.8rem; /* Adjust the font size */
}
</style>

