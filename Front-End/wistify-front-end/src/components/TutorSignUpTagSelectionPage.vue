<template>
  <div class="flex flex-col items-center justify-center bg-white min-h-screen">
    <h2 class="text-2xl font-semibold mb-4">Select Learning Subjects</h2>

    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
      <div
          v-for="subject in subjects"
          :key="subject.id"
          @click="toggleSubject(subject)"
          :class="{ 'bg-green-500 text-white': selectedSubjects.includes(subject.id) }"
          class="cursor-pointer p-3 border border-gray-300 rounded-md text-center hover:bg-green-200 transition-all duration-300"
      >
        {{ subject.name }}
      </div>
    </div>

    <div class="mt-4">
      <button @click="goBack" class="text-gray-600 hover:underline mr-4">Back</button>
      <button @click="createAccount" class="bg-blue-500 text-white py-2 px-4 rounded-md">Create Account</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subjects: [
        { id: 1, name: 'Math' },
        { id: 2, name: 'Physics' },
        { id: 3, name: 'Chemistry' },
        { id: 4, name: 'Biology' },
        // Add more subjects as needed
      ],
      selectedSubjects: [],
    };
  },
  methods: {
    toggleSubject(subject) {
      const index = this.selectedSubjects.indexOf(subject.id);
      if (index === -1) {
        this.selectedSubjects.push(subject.id);
      } else {
        this.selectedSubjects.splice(index, 1);
      }
    },
    goBack() {
      // Implement navigation logic to go back to the previous page
      this.$router.push({ path: '/' })
    },
    createAccount() {
      // Implement logic to create an account with selected subjects
      console.log('Creating account with selected subjects:', this.selectedSubjects);
    },
  },
};
</script>

<style scoped>
/* Add your scoped styles here */
.flex {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.grid {
  display: grid;
}

.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.sm\:grid-cols-3 {
  @media (min-width: 640px) {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.md\:grid-cols-4 {
  @media (min-width: 768px) {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

.lg\:grid-cols-5 {
  @media (min-width: 1024px) {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }
}

.gap-4 {
  gap: 1rem;
}

.border {
  border-width: 1px;
}

.border-gray-300 {
  border-color: #d1d5db;
}

.p-3 {
  padding: 0.75rem;
}

.rounded-md {
  border-radius: 0.375rem;
}

.text-center {
  text-align: center;
}

.hover\:bg-green-200:hover {
  background-color: #a7f3d0;
}

.transition-all {
  transition-property: all;
  transition-duration: 300ms;
}

.duration-300 {
  transition-duration: 300ms;
}

.mt-4 {
  margin-top: 1rem;
}

.text-gray-600 {
  color: #6b7280;
}

.hover\:underline:hover {
  text-decoration: underline;
}

.bg-blue-500 {
  background-color: #2563eb;
}

.text-white {
  color: #fff;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}
</style>
