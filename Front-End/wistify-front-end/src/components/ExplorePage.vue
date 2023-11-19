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
      ]
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

