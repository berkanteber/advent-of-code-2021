import os
from itertools import product

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()

xyz_coord = tuple[int, int, int]


def rotate_along_xy_once(x: int, y: int, z: int) -> xyz_coord:
    return (-y, x, z)


def rotate_along_yz_once(x: int, y: int, z: int) -> xyz_coord:
    return (x, -z, y)


def rotate_along_xz_once(x: int, y: int, z: int) -> xyz_coord:
    return (-z, y, x)


def rotate_along_plane(coord: xyz_coord, plane: str, *, count: int) -> xyz_coord:
    if count == 0:
        return coord

    rotation_func = {
        "xy": rotate_along_xy_once,  # x becomes -y, y becomes x
        "yz": rotate_along_yz_once,  # y becomes -z, z becomes y
        "xz": rotate_along_xz_once,  # x becomes -z, z becomes x
    }[plane]

    return rotate_along_plane(rotation_func(*coord), plane, count=(count - 1))


def rotate(coord: xyz_coord, rotate_counts: tuple[int, int, int]) -> xyz_coord:
    xy_count, yz_count, xz_count = rotate_counts
    coord = rotate_along_plane(coord, "xy", count=xy_count)
    coord = rotate_along_plane(coord, "yz", count=yz_count)
    coord = rotate_along_plane(coord, "xz", count=xz_count)
    return coord


def solve(data: str) -> int:
    scanner_beacons = []
    for scanner_str in data.split("\n\n"):
        beacons = []
        _, _, beacons_str = scanner_str.partition("\n")
        for beacon_str in beacons_str.split():
            x_str, y_str, z_str = beacon_str.split(",")
            beacons.append((int(x_str), int(y_str), int(z_str)))
        scanner_beacons.append(beacons)

    scanner0_location = (0, 0, 0)
    scanner0_rotate_counts = (0, 0, 0)
    scanners = {0: (scanner0_location, scanner0_rotate_counts)}
    known_scanners = {0}
    while len(scanners) < len(scanner_beacons):
        reference_idx = known_scanners.pop()
        ref_loc, ref_rot_count = scanners[reference_idx]
        ref_loc_x, ref_loc_y, ref_loc_z = ref_loc

        reference_beacons = []
        for beacon in scanner_beacons[reference_idx]:
            x, y, z = rotate(beacon, ref_rot_count)
            reference_beacons.append((ref_loc_x + x, ref_loc_y + y, ref_loc_z + z))

        for i, relative_beacons in enumerate(scanner_beacons):
            if i in scanners:
                continue

            found = False
            beacon_pairs = product(reference_beacons, relative_beacons)
            for reference_beacon, relative_beacon in beacon_pairs:
                ref_x, ref_y, ref_z = reference_beacon

                tried_locations = set()
                for rot_x, rot_y, rot_z in product(range(4), repeat=3):
                    rotate_counts = (rot_x, rot_y, rot_z)
                    rel_x, rel_y, rel_z = rotate(relative_beacon, rotate_counts)
                    location = (ref_x - rel_x, ref_y - rel_y, ref_z - rel_z)
                    if location in tried_locations:
                        continue
                    tried_locations.add(location)
                    loc_x, loc_y, loc_z = location

                    overlap_count = 0
                    ref_beacons = set(reference_beacons)
                    for beacon in relative_beacons:
                        x, y, z = rotate(beacon, rotate_counts)
                        if (loc_x + x, loc_y + y, loc_z + z) in ref_beacons:
                            overlap_count += 1
                            if overlap_count == 12:
                                scanners[i] = (location, rotate_counts)
                                known_scanners.add(i)
                                found = True
                                break

                    if found:
                        break

                if found:
                    break

    distances = []
    for i in range(len(scanners)):
        (x1, y1, z1), _ = scanners[i]
        for j in range(i + 1, len(scanners)):
            (x2, y2, z2), _ = scanners[j]
            distances.append(abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))

    return max(distances)


example_data = """\
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""

assert solve(example_data) == 3621

print(solve(data))  # 11828
