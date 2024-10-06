<script lang="ts">
    export let amount;
    import ky from "ky";
    import { z } from "zod";
    import { createQuery } from "@tanstack/svelte-query";
    let name = "New Wallet";
    const dataType = z.object({ dollars: z.number() });
    type Data = z.infer<typeof dataType>;
    const query = createQuery({
        queryKey: ["check"],
        queryFn: () => ky.post<Data>("/data").json(),
    });
</script>

<section class="p-2 text-red-500">
    {name} - {amount} |
    {#if $query.isSuccess}
        <span>{$query.data?.dollars}</span>
    {:else if $query.isError}
        <span>Error: {$query.error}</span>
    {/if}
</section>
