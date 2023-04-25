# repro-full-control-broken

Suspect that [#700](https://github.com/pynecone-io/pynecone/pull/700) introduced the
issue reproduced by this example.

## `tox -e py-pynecone-0.1.24`

Open browser to [http://localhost:3000](http://localhost:3000) and type input
into text field. It should be displayed in near real time above the text box.

Check the "Slow?" box to toggle a 0.5 second server-side delay, which has
significant effects on the UX.

## `tox -e py-pynecone-main`


Open browser to [http://localhost:3000](http://localhost:3000) and type input
into text field.

A warning is displayed in browser console, event is NOT sent to the server side.

```
Warning: State updates from the useState() and useReducer() Hooks don't support the second callback argument. To execute a side effect after rendering, declare it in the component body with useEffect().
```