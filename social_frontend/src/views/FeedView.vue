<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="main-center col-span-2 space-y-4">
                <div class="bg-white border border-gray-200 rounded-lg">
                    <FeedForm v-bind:user="null" v-bind:posts="posts" />
                </div>

                <!-- <div class="p-4 bg-white border border-gray-200 rounded-lg">
          <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center space-x-6">
              <img
                src="https://i.pravatar.cc/300?img=70"
                class="w-[40px] rounded-full"
              />

              <p><strong> Image post</strong></p>
            </div>

            <p class="text-gray-600">18 minutes ago</p>
          </div>

          <img
            src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80"
            class="w-full rounded-lg"
          />

          <div class="my-6 flex justify-between">
            <div class="flex space-x-6">
              <div class="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                  ></path>
                </svg>

                <span class="text-gray-500 text-xs">{{ post.likes_count }} likes</span>
              </div>

              <div class="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
                  ></path>
                </svg>

                <span class="text-gray-500 text-xs">0 comments</span>
              </div>
            </div>

            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
                ></path>
              </svg>
            </div>
          </div>
        </div> -->

                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                    <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
                </div>
            </div>
        </div>
        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import PeopleYouMayKnow from "@/components/peopleYouMayKnow.vue";
import Trends from "@/components/Trends.vue";
import FeedItem from "@/components/FeedItem.vue";
import FeedForm from "@/components/FeedForm.vue";
import axios from "axios";

export default {
    name: "FeedView",
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        FeedForm,
    },
    data() {
        return {
            posts: [],
            body: "",
            url: null,
        };
    },
    mounted() {
        this.getFeed();
    },
    methods: {
        onFileChnage(e) {
            // console.log(e.target.file);
            const file = e.target.files[0];
            this.url = URL.createObjectURL(file);
        },
        deletePost(id) {
            this.posts = this.posts.filter((post) => post.id !== id);
        },
        getFeed() {
            axios
                .get("api/posts/")
                .then((response) => {
                    // console.log("data", response.data);

                    this.posts = response.data;
                })
                .catch((error) => {
                    console.log("error", error);
                });
        },
        // submitPost() {
        //   console.log("Submit Form ", this.body);

        //   let context = { body: this.body };
        //   axios
        //     .post("api/posts/create/", context)
        //     .then((response) => {
        //       console.log("data", response.data);

        //       this.posts.unshift(response.data);
        //       this.body = "";
        //     })
        //     .catch((error) => {
        //       console.log("error", error);
        //     });
        // },
    },
};
</script>
