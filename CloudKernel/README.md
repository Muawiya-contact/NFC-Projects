# CloudKernel

CloudKernel is a Java concurrency simulator with a Swing dashboard that models a
hypervisor managing virtual machines. A configurable number of VM threads boot
together, compete for shared CPU, memory, and network resources, and synchronize
at the end of each execution cycle, while the GUI shows their state, resource
usage, and a live event log in a dark-theme monitor layout.

<img src="img/banner.png">

## How it works

- Boot phase: a CountDownLatch holds the VMs until four boot tasks complete.
- Runtime phase: each VM runs a configured number of cycles with randomized
  workload durations.
- Resource phase: VMs acquire CPU, memory, and network permits from fair
  semaphores, with a timeout so contention never deadlocks.
- Synchronization phase: all VMs rendezvous at a CyclicBarrier before starting
  the next cycle.

The main window shows a header with a digital clock, a boot panel with the
latch countdown, one card per VM (state, priority, progress, held resources),
a semaphore slot view for each resource, a barrier panel with arrival dots,
a color-coded event log, and a stats/control bar. Logs stream to the terminal
and the GUI at the same time, and stats track cycles, operations, contentions,
timeouts, and uptime. Worker threads never touch Swing directly; all UI updates
go through SwingUtilities.invokeLater.

Source lives under `src/` in packages: `config` (ConfigLoader), `core`
(BootManager, ClockSynchronizer), `entities` (VirtualMachine, ResourceManager,
VM state/priority/stats), `shutdown` (ShutdownManager), `ui` (the dashboard
panels), and `utils` (GUILogger, StatsCollector). `Main.java` is just the GUI
entry point. Design details are in `ARCHITECTURE.md`, and the proposal, report,
and slides are in `doc/`.

## Configuration

Edit `config.properties` before running. It sets the VM count, cycles per VM,
permit counts for the CPU/memory/network semaphores, min/max task duration,
acquire timeout, GUI options (enabled, theme, font), logging level, and whether
stats collection is on.

## Build and run

From the CloudKernel root on Windows (PowerShell):

```powershell
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse src -Filter *.java | ForEach-Object { $_.FullName })
java -cp "bin;." Main
```

On Linux/macOS the equivalent is:

```bash
javac -encoding UTF-8 -d bin $(find src -name '*.java')
java -cp "bin:." Main
```

## Credits

Operating Systems project, 4th semester BSAI 2k24, Department of Artificial
Intelligence, NFC Institute of Engineering & Technology, Multan.
Submitted to Mam Amara Nadeem (ammara.visiting@nfciet.edu.pk) on March 03, 2026.

Team: Muawiya Amir (2k24_BSAI_72, 2k24bsai72@undergrad.nfciet.edu.pk),
Ali Raza (2k24_BSAI_44, 2k24bsai44@undergrad.nfciet.edu.pk),
Muhammad Arslan Nasir (2k24_BSAI_26, 2k24bsai26@undergrad.nfciet.edu.pk).
