export default {
  async fetch(request, env) {
    const res = await env.ASSETS.fetch(request);
    if (res.status === 404) {
      const page = await env.ASSETS.fetch("/404.html");
      return new Response(page.body, {
        status: 404,
        headers: page.headers
      });
    }
    return res;
  }
};
